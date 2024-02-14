from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
element = driver.find_element(By.ID,"my-text-id").click()
time.sleep(5)
element2 = driver.find_element(By.CLASS_NAME,"form-control")
time.sleep(5)
element3 = driver.find_element(By.TAG_NAME,"label")
time.sleep(5)
element4 = driver.find_element(By.TAG_NAME,"label")
time.sleep(5)
element5 = driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[2]/button')

btn1 = driver.find_element(By.XPATH,'//*[@id="my-check-2"]').click()
time.sleep(5)
btn2 = driver.find_element(By.XPATH,'//*[@id="my-radio-2"]').click()
time.sleep(5)
btnSubmit = driver.find_element(By.XPATH,'/html/body/main/div/form/div/div[2]/button').click()

