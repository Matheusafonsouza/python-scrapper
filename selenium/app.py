import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('window-size=400,800')
# options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get('https://www.airbnb.com/')

sleep(10)

driver_input = driver.find_element_by_tag_name('input')
driver_input.send_keys('São paulo')
driver_input.submit()

sleep(3)
driver.find_element_by_css_selector('button > img').click()
sleep(3)
driver.find_element_by_xpath("//button[text()='Pular']").click()
sleep(3)
driver.find_element_by_xpath("//button[text()='Pular']").click()

web_content = driver.page_source

sleep(3)

web = BeautifulSoup(web_content, 'html.parser')
print(web.prettify())