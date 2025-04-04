import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Vegetables and Fruits']").send_keys("ber")
driver.find_element(By.XPATH, "//button[@class='search-button']").click()

# in this time image load take a time, so we time.sleep
# find_elements except from implicitly_wait
time.sleep(3)

count = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print("the total count of element :",len(count))
for i in count:
    i.find_element(By.XPATH, "div/button").click()
    #assert i.find_element(By.XPATH, "div/button").is_selected()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()


'''
# explicitly
# target one particular element
# which element take more 5 sec that element we target and we give more time
# it's not globally
# we can create object of WebDriverWait and we give parameter of global driver,expect waiting time
# then we define which element we target and wait
# that we use wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
# expected_conditions - we tell what give condition
# presence_of_element_located - that element is how present (locator or text or ect..)
# and also give element locator
'''

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
result = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
print(result)




