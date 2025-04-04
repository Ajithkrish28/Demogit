'''
handle browser soft list

we have save the item in list and sort list save other variable and validate

'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
time.sleep(3)
driver.maximize_window()
driver.implicitly_wait(5)

BrowserList = []

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()  # we can click browser sort

veg_web_element = driver.find_elements(By.XPATH, "//tbody/tr/td[1]")  # we store list of elements

for veg in veg_web_element:
    BrowserList.append(veg.text)    # rext is append in BrowserList

Original_element = BrowserList.copy()   # before we sort the BrowserList, we take copy that

BrowserList.sort()

assert BrowserList ==Original_element

