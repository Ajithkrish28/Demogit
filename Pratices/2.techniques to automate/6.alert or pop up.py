import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# it is alert or pop up ( msg in screen top)
# it's not HTML code it a JavaScript msg
# so, we switch or change to alert mode.

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Ajith")   # we found element and give value
driver.find_element(By.CSS_SELECTOR, "input[value='Alert']").click()   #after given value put click.

# now we do change to alert mode
alert = driver.switch_to.alert  # we change mode and store in object
print(alert.text)
alert.accept()   # click a positive value( ok ),# it's positive


# negative
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Ajith")
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()

# now we change mode

alert = driver.switch_to.alert
value = alert.text
print(value)
alert.dismiss()   # it's a negative value( cancel )



time.sleep(3)