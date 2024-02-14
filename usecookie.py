from selenium import webdriver
import pickle

cookies = pickle.load(open('cookies.pkl','rb'))
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome()
driver.get('https://th.wikipedia.org/') # ให้เข้าเว็บก่อนครั้งนึง
for c in cookies: # ติดตั้งคุกกี้เข้าไป
    driver.add_cookie(c)
driver.get('https://th.wikipedia.org/') # เปิดเว็บหลังจากที่ติดตั้งคุกกี้แล้ว