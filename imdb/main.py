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
    # url = "https://www.imdb.com/search/title/?title_type=feature&release_date=2023-01-01,2023-12-31"
    testurl = "https://www.imdb.com/search/title/?title_type=feature&release_date=1988-01-01,1988-01-09"
    options = Options()
    options.headless = True

    driver = webdriver.Chrome(options=options)
    driver.get(testurl)

    wait = WebDriverWait(driver, 10)
    closeCookies = wait.until(EC.presence_of_element_located(
        (By.XPATH, ("//*[@data-testid='reject-button']"))))
    closeCookies.click()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


if __name__ == "__main__":
    main()
