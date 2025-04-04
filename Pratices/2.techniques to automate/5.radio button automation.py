import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

# we don't have a unique attribute or locator we use this type
# all radio button are stored in variable ( we use find_elements() )

radio_button = driver.find_elements(By.CSS_SELECTOR, "input[name='radioButton']")

print(len(radio_button))

# we know  radio buttons are not changeable so, we give index value and click

radio_button[2].click()

assert radio_button[2].is_selected()



# is displayed
# displayed or nor

assert driver.find_element(By.ID, "displayed-text").is_displayed()  # check is this display or not, if not display get error
driver.find_element(By.ID,"hide-textbox").click()   # it's click a hide
#assert driver.find_element(By.ID, "displayed-text").is_displayed()  - in cause in line code is execute get error( display is hide, so, we get error)



time.sleep(3)