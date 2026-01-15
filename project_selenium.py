from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
import pandas as pd
import time

iisttt = []

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")

elem = driver.find_element(By.NAME,"q")
elem.send_keys("phone")
elem.send_keys(Keys.RETURN)


p = driver.find_elements(By.CLASS_NAME,"CMXw7N")
for i in p:
    name = i.text
    iisttt.append(name)

print(name)

f = pd.DataFrame(iisttt)
f.to_excel("hhhhh.xlsx")
# f.to_csv("hhh.csv")

time.sleep(2)
driver.quit()