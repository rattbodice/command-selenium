from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get('https://th.wikipedia.org/wiki/โตเกียว')
link = driver.find_element('link text','ญี่ปุ่น')
link.click()