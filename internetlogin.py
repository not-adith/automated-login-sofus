from selenium import webdriver
from selenium.webdriver.common.by import By
browser= webdriver.Chrome("D:\#workspace\chromedriver_win32\chromedriver.exe")
browser.get("http://1.1.1.1:8090/httpclient.html")
username=browser.find_element(By.CSS_SELECTOR, "#username")
password=browser.find_element(By.CSS_SELECTOR, "#password")
submit=browser.find_element(By.CSS_SELECTOR, "#loginbutton")
username.send_keys("GCEK")
password.send_keys("2023")
submit.click()
browser.quit()
