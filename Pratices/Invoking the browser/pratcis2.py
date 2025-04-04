from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()

items = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for i in items:
    if i.find_element(By.XPATH, "div/h4/a").text ==  "Blackberry":
        i.find_element(By.XPATH, "//div[@class='card h-100']/div/button").click()

driver.find_element(By.CLASS_NAME, "btn-primary").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
result = driver.find_element(By.CLASS_NAME, "alert-success").text

if "Success! Thank you!" in result:
    print("good")