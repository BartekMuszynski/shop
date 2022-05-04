from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
s = Service("C:\\Users\\bartosz.muszynski\\Desktop\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
# driver.get("https://wp.pl/")
# time.sleep(5)
# x = driver.find_element(By.XPATH,'//a[@href="https://poczta.wp.pl"]').click()
driver.get("https://www.geeksforgeeks.org/")
x = driver.find_element(By.PARTIAL_LINK_TEXT,"Practice").click()