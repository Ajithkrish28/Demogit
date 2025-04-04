from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# unique locator (ID,NAME,CLASS NAME) or unique attribute is not in element we use this type.
# we use find elements
# store in variable

check_box = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(check_box))

#take one by one from check_box variable
# and check the element attribute is equal to attribute value
for check in check_box:
    if check.get_attribute("value") == "option2":
        check.click()

