from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# import chromedriver_autoinstaller
import re

options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")

# For local testing
# chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')

def scrape_myprotein():
    driver.get('https://www.myprotein.com.sg/')
   
    myprotein_banner_class = 'stripBanner_text'
    myprotein_banner_text = driver.find_elements(By.CLASS_NAME, myprotein_banner_class)

    for child in myprotein_banner_text:
        search = re.findall('.*\s\d*%\s.*', child.text)

    for index, text in enumerate(search):
        search[index] = text.strip()

    return ' '.join(search)