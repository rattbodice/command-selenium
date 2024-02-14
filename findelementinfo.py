from selenium import webdriver
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.co.th?hl=th')
q = driver.find_element('name','q')
q.send_keys("test")
q.send_keys(Keys.ENTER)
print(q.size)
print(q.location)
print(q.tag_name)