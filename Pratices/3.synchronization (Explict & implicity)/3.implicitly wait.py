import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.implicitly_wait(5)    # global waiting time.


# implicitly_wait  -- it's help us for element is not find immediately or not display immediately wait maximum 5 second.
# element find 1 or 2 second then execute next code,
# but sleep is what happen in there that no matter, it just closed some seconds, not wait for find element



driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# here we use sleep, because we give find_elements, it's return list of element, sometime page loaded take sometime,
# but selenium not take time for page load, it returned empty list( list[] ) immediately.
# so, we give sleep for page loaded
# implicitly not working in find_elements, this only exception ( rest all element work in implicitly )

time.sleep(3)
count = driver.find_elements(By.XPATH, "//div[@class='products']/div")
#print(len(count))
assert len(count) > 0

# chain method ( already maximum locator in count variable now we give remain locator from count )
for i in count:
    i.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

result = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
print(result)



