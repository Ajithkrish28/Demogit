import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

name = driver.window_handles
driver.switch_to.window(name[1])
mails = driver.find_element(By.CSS_SELECTOR, ".red").text
mail = mails.split()
print(mail)
driver.close()
driver.switch_to.window(name[0])
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(mail[4])
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("12345678")
drop = Select(driver.find_element(By.CSS_SELECTOR, "select[class='form-control']"))
drop.select_by_visible_text("Teacher")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".alert")))
print(driver.find_element(By.CSS_SELECTOR, ".alert").text)