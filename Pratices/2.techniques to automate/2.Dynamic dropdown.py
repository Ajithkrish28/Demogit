import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()

# we find drop down element
driver.find_element(By.XPATH, "//input[@id='autosuggest']").send_keys("ind")



# in HTML code not in select we didn't use select class,dynamic dropdown we use another method
# we store some element like a same locator, because dynamic dropdown is values change sometimes, seo, we store all elements in variable.

count = driver.find_elements(By.XPATH, "li[class='ui-menu-item'] a")  # find.elements is return a list and store in variable.
print(len(count))

# we check india in count if there india will click.
for country in count:
    if country == "India":
        country.click()
        break

time.sleep(3)