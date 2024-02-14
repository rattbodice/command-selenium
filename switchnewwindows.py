from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.co.th?hl=th') # หน้าเว็บในแท็บแรก
driver.switch_to.new_window('tab') # เปิดแท็บใหม่
driver.get('https://th.wikipedia.org') # หน้าเว็บในแท็บใหม่
print(driver.window_handles) # ได้ ['CDwindow-3A12304FDB753B8628A5EBCF6105A719', 'CDwindow-441F17D942BEFAA1AD2A2F044F24CC63']