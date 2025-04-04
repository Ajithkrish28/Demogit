import time

from selenium import webdriver

from selenium.webdriver.common.by import By     # it's for we use BY operators so we have import

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")


#  Identifiers is used  for fine the element
# ID, NAME, Classname, LinkText,Xpath, CSSSelector  ( selenium have provided the these locator identifiers.)
# NAME, ID have is developer is what they give that one we have use.

driver.find_element(By.NAME, "email").send_keys("hello@gamil.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

time.sleep(4)