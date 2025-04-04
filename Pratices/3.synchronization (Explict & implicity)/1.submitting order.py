'''in this topic is how put order and place'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# find the element and give some input like ber and what in ber all element are get.

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
driver.find_element(By.CSS_SELECTOR, "button[class='search-button']").click()

#now there are 3 element if upcoming days I add another element that element also add and get count
# so we use find elements ( we get all element common locator path ) and store in variable
count = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(count))


time.sleep(3)