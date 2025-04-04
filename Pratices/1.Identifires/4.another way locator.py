import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client")

driver.maximize_window()

# Link Text is a any link in the webpage  that link access to use link text and link text HTML in tag a.

driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# the element are not unique(unique locator or attribute  values) or no attribute is here so, we use another way of XPATH and CSS Selector
# is this use to find path way

# XPATH - //parent / child / child tag ---> //form/div[1]/input([1] is this a number of element

driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("Hello@gmail.com")

# CSS Selector - parent child childtag ---> form div:nth-child(2) input, (2) is a number of elements

driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("123456")

driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("123456")

# below code is find text and access
# is this only in XPATH
#syntax --> // tag[text()='text content'] ---> //button[text()='Save New Password']

driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(3)