import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expected = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
actual = []
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ber")
driver.find_element(By.CSS_SELECTOR, '.search-button').click()
time.sleep(3)

items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print("The total count is :",len(items))
assert len(items) > 0

for i in items:
    actual.append(i.find_element(By.XPATH, "h4").text)
    i.find_element(By.XPATH, "div/button").click()
print(actual)


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


prices = driver.find_elements(By.XPATH, "//tbody/tr/td[5]/p")
sum = 0

for price in prices:
    sum = sum + int(price.text)

total = int(driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text)

assert sum == total

driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)
Discount  = float(driver.find_element(By.CSS_SELECTOR, "span[class='discountAmt']").text)
print("the discount amount is :",Discount )
assert Discount  < total
print("total Amount is more than Discount Amount")

