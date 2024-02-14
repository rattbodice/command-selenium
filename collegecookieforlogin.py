from selenium import webdriver
import pickle

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome()
driver.get('https://th.wikipedia.org/w/index.php?title=พิเศษ:ล็อกอิน')
# เติมชื่อผู้ใช้
name_box = driver.find_element('name','wpName')
name_box.send_keys('ชื่อผู้ใช้')
# เติมรหัสผ่าน
password_box = driver.find_element('name','wpPassword')
password_box.send_keys('รหัสผ่าน')
# กดติ๊กเพื่อให้อยู่ในระบบต่อไป
remember_box = driver.find_element('name','wpRemember')
remember_box.click()
name_box.submit() # ซับมิตแบบฟอร์มเพื่อล็อกอิน
cookies = driver.get_cookies() # ดึงคุ้กกี้หลังการล็อกอิน
pickle.dump(cookies,open('cookies.pkl','wb')) # บันทึกคุกกี้ลงไฟล์ด้วย pickle
driver.quit()

#หลังจากรันก็จะมีไฟล์ cookies.pkl