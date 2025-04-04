import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("ind")

country = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")

print(len(country))

for i in country:
    if i.text == "India":
        i.click()

# print the dynamic value
# we didn't use text command, because text command is only for predefined values( already in there)
# but dynamic value is we given, so, we didn't use text command,
# so, we use get_attribute("value"), it's access the value and print value

print(driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value"))

#assert driver.find_element(By.XPATH, "//input[@id='autosuggest']").get_attribute("value") == "India"  # validation

time.sleep(3)