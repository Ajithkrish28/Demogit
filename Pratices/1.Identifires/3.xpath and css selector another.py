import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ajith")
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

# CSS Selector another way are - #id value (#id value), .class name( .class name value)

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
message = driver.find_element(By.CSS_SELECTOR , ".alert-success").text
print(message)

assert "Success" in message

# Xpath another selector

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Ajith")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()   # clear a text in box

time.sleep(3)



