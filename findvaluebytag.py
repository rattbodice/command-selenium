from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome()
driver.get('https://www.google.co.th/search?q=กาแฟ&hl=th')
lis_h3 = driver.find_elements('tag name','h3')
for h3 in lis_h3:
    print('~',h3.text)
driver.quit()