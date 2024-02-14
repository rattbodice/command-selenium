from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get('https://th.wikipedia.org/wiki/ราเม็ง')
driver.save_screenshot('phapnacho.png') #บันทึกหน้าจอ