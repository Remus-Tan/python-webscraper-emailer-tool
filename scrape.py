from selenium import webdriver
import chromedriver_autoinstaller
import re

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

def scrape_myprotein():
    driver.get('https://www.myprotein.com.sg/')
   
    myprotein_banner_class = 'stripBanner_text'
    myprotein_banner_text = driver.find_elements_by_class_name(myprotein_banner_class)

    for child in myprotein_banner_text:
        search = re.findall('\s\d*%\s', child.text)

    for index, text in search:
        search[index] = text.trim()

    return search

