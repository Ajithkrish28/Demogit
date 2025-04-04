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


'''sum validation '''

prices = driver.find_elements(By.XPATH, "//tbody/tr/td[5]/p") # we store all element in variable
sum = 0        # we put sum = 0 for add all integer
for price in prices:
    sum = sum + int(price.text)   # text is return only str we change to int and add one by one from variable elements

print("the total amount of purchase : ",sum)

compare_amount = int(driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text)
print(compare_amount)
assert sum == compare_amount   # it is a validation



driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
result = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
print(result)




