from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com.br/')

driver_input = driver.find_element_by_css_selector("[title^='Pesquisar']")
driver_input.send_keys('doctor strange')