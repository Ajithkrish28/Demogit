import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath and CSS selector
# both are any element access in webpage.but we have small syntax, that only we use, other(name,id) these are no syntax
# Xpath  --> syntax -  //tag name[@attribute = 'attribute value'] we use(' ' )
# CSS selector --> syntax -  tag name[attribute='attribute values']  -- > //input[@type='submit']   we use(' ' )



driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ajith")
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)


# assertion (validation), it is a some string present in variable (message).in-cause not this string not in variable we get error.
assert "Success" in message

time.sleep(3)