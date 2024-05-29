import csv
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def main():
    csv_filename = "../scrapedMovies/imdb.csv"
    if os.path.exists(csv_filename) == False:
        os.makedirs(os.path.dirname(csv_filename))
        with open(csv_filename, mode='x', ) as f:
            f.close()

    # Only movies from 2023 to now (29.05.2024), 10 genres
    urlMain = "https://www.imdb.com/search/title/?title_type=feature&release_date=2023-01-01,2024-05-29&genres="
    genres = ["action", "adventure", "biography", "comedy",
              "crime", "documentary", "drama", "romance", "horror"]
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    for genre in genres:
        currentUrl = urlMain + genre
        driver.get(currentUrl)

        wait = WebDriverWait(driver, 10)
        try:
            closeCookies = wait.until(EC.presence_of_element_located(
                (By.XPATH, ("//*[@data-testid='reject-button']"))))
            closeCookies.click()
        except:
            print("No cookies to close")

        scrollPage = driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        moreButtonClass = "//button[@class='ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-base ipc-btn--theme-base ipc-btn--on-accent2 ipc-text-button ipc-see-more__button']"
        moreButtonWait = wait.until(EC.presence_of_element_located(
            (By.XPATH, moreButtonClass)))

        while True:
            scrollPage
            moreButtonWait
            try:
                driver.execute_script("arguments[0].click();", driver.find_element(
                    by=By.XPATH, value=moreButtonClass))
            except:
                print("End of page")
                break
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        movies = soup.find_all("li", class_="ipc-metadata-list-summary-item")

        with open(csv_filename, mode='w', newline="", encoding="utf-8-sig") as csvfile:
            writer = csv.writer(csvfile)
            header = ['Genre', 'Name', 'Year', 'Rating', "Rating amount"]
            writer.writerow(header)
            for movie in movies:
                name = movie.find(
                    "div", class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b189961a-9 iALATN dli-title").a.h3.text.split(". ")[1]
                try:
                    year = movie.find(
                        "div", class_="sc-b189961a-7 feoqjK dli-title-metadata").span.text
                except:
                    year = "N/A"

                try:
                    rating = movie.find(
                        "div", class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").span.text.split("(")[0]
                    rating = "N/A" if rating == "Rate" else rating[:-1]
                except:
                    rating = "N/A"

                try:
                    amount = movie.find(
                        "div", class_="sc-e2dbc1a3-0 ajrIH sc-b189961a-2 fkPBP dli-ratings-container").span.text.split("(")[1]
                    amount = amount[:-1]
                except:
                    amount = "N/A"

                writer.writerow([genre, name, year, rating, amount])


if __name__ == "__main__":
    main()
