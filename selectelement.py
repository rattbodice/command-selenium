from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--window-size=380,450')
driver = webdriver.Chrome(options=options)
driver.get('https://th.wikipedia.org/w/index.php?title=พิเศษ:ล็อกอิน')
chongtick = driver.find_element('name','wpRemember')
print(chongtick.is_selected()) # ได้ False
chongtick.click() # กดติ๊กช่อง
print(chongtick.is_selected()) # ได้ True
time.sleep(1) # รอเวลาสักพักให้ผลการติ๊กแสดงให้เห็นในหน้าจอ
driver.save_screenshot('phapnacho.png')
driver.quit()