import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
driver.find_elements(By.CSS_SELECTOR, "button[class='search-button']").click()

count = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(count))
# assert count > 0

#chain element ( maximum path locator in count variable again continue from count )
# we not use driver, driver consider to whole page, we need only count locator )
# //div[@class='products']/div/div/button in this locator we use separately.   //div[@class='products']/div - already store in count
for i in count:
    i.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()


check = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
print(check)
# assert driver.find_element(By.XPATH, "//span[@class='promoInfo']").text == "Code applied ..!"


'''
This program will get error because one page to go another page it's take a some second time and get wait, but this program we not give wait

we see next lecture for implicit and explicit 
'''
