from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome()
driver.get('https://www.google.co.th/search?q=มังกร&hl=th')
lis_gh3 = driver.find_elements('css selector','.g h3')
for gh3 in lis_gh3:
    print('~',gh3.text)
driver.quit()