from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome()
driver.get('https://th.wikipedia.org/wiki/ซุนดะโมจิ')
el = driver.find_element('xpath','//*[@id="mw-content-text"]/div[1]/p/a[1]')
print(el.get_attribute('href'))
print(el.text)
print(el.tag_name)