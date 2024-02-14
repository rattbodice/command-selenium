from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless') #การซ่อนบราวเซอร์ไม่ต้องแสดง
options.add_argument('--window-size=400,530')
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.co.th/search?q=ง่วง&hl=th')
lis_g = driver.find_elements('class name','g')
print(len(lis_g))
for g in lis_g:
    print(g.location)
driver.save_screenshot('phapnacho.png')
driver.quit()