import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

driver.find_element(By.NAME, "name").send_keys("Ajith")
driver.find_element(By.NAME, "email").send_keys("Hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234567")
driver.find_element(By.ID,"exampleCheck1").click()


#Drop Down - use a select class and create object, HTML in select tag that is static drop down
#dropdowm is object from select class.

dropdown = Select(driver.find_element(By.XPATH, "//form/div[5]/select"))
dropdown.select_by_visible_text("Male")    # static drop down have many option to find locator we see 2,it's a  text base selector
dropdown.select_by_index(1)  #it's index base selector


driver.find_element(By.ID,"inlineRadio1").click()
driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
driver.find_element(By.CLASS_NAME, "ng-pristine").send_keys("Kumar")

time.sleep(4)