import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def main():
    SCROLL_PAUSE_TIME = 2
    moreButtonExists = True

    url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2023-01-01,2023-12-31"
    testurl = "https://www.imdb.com/search/title/?title_type=feature&release_date=1988-01-01,1988-01-09"
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    # driver.get(url)
    driver.get(testurl)

    wait = WebDriverWait(driver, 10)
    closeCookies = wait.until(EC.presence_of_element_located(
        (By.XPATH, ("//*[@data-testid='reject-button']"))))
    closeCookies.click()

    scrollPage = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")

    moreButtonClass = "//button[@class='ipc-btn ipc-btn--single-padding ipc-btn--center-align-content ipc-btn--default-height ipc-btn--core-base ipc-btn--theme-base ipc-btn--on-accent2 ipc-text-button ipc-see-more__button']"
    moreButtonWait = wait.until(EC.presence_of_element_located(
        (By.XPATH, moreButtonClass)))

    while True:
        scrollPage
        moreButtonWait
        driver.execute_script("arguments[0].click();", moreButtonWait)
        moreButtonWait
        try:
            driver.find_element(
                By.XPATH, "//span[contains(@class, 'ipc-see-more')]/button[contains(@class, 'ipc-btn--single-padding')]")
        except:
            print("End of page")
            break


if __name__ == "__main__":
    main()
