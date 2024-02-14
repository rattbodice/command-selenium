from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.co.th?hl=th')
q = driver.find_element('name','q')
q.send_keys('ใครมา')
q.send_keys(Keys.SHIFT+Keys.LEFT+Keys.LEFT) # ลากคลุมไปทางซ้าย ๒ ช่อง
q.send_keys(Keys.CONTROL+'c') # คัดลอกข้อความที่ลากคลุม
q.send_keys(Keys.CONTROL+'a') # ลากคลุมข้อความทั้งหมด
q.send_keys(Keys.DELETE) # ลบข้อความทั้งหมด
q.send_keys('ไม่')
q.send_keys(Keys.CONTROL+'v') # แปะข้อความ