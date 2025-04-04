'''
getting value from table

in this , we use unique locator

because , some rows and column are dynamically change that place.

so, this way use attribute, values are change but attribute not change

'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.maximize_window()
fruit = "Papaya"    # we save fruit name in variable
time.sleep(3)
# colum will be change so, we find price in locator and get attribute value( in cause column change , will variable value change)
column = driver.find_element(By.XPATH, "//div[text()='Price']").get_attribute("data-column-id")  #//div[text()='Price'] locator attribute values and store


# below locator goes child to parent and parent to child
#  to parent use to //tag name[@attribute='value']/parent:: parent tag name
# "+fruit+" - which fruit name save and pass that particular fruit price are getting
actual_price = driver.find_element(By.XPATH, "//div[text()='"+fruit+"']/parent::div/parent::div/div[@id='cell-"+column+"-undefined']/div").text
print(actual_price)