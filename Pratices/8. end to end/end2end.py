import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(5)
driver.implicitly_wait(5)

'''
special path: regular expression

CSS_SELECTOR = tag[attribute* = 'attribute value']- a[href*='shop'] - bit of attribute value
XPATH   //tag[contain(@attribute, 'attribute value')] -//a[contains(@href,'shop')] - bit of attribute value

'''


driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='card h-100']")))
items = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for item in items:
    if item.find_element(By.XPATH, "div/h4").text == "Blackberry":
        item.find_element(By.XPATH, "div[@class='card-footer']/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()



driver.find_element(By.XPATH, "//button[contains(@class, 'btn btn-success')] ").click()
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
result = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in result

