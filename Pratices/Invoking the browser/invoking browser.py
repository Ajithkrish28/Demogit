import time

from selenium import webdriver    # we have import webdriver from selenium, because webdrive is invoke(call) the browser.

driver = webdriver.Chrome()    #Chrome is a class it's a already build in python.driver is object of Chrome class.it is a representative.

driver.get("https://rahulshettyacademy.com")   # it's a launch URL and get website.

driver.maximize_window()    #it is a, the window page is maximize

print(driver.title)    #it is get a webpage title and we need to print title so we give print statement.

print(driver.current_url)    #it is use for sometime url redirect or url was changed, so, that url get and print.


time.sleep(5)   # selenium close the webpage one complete the process it work very fact so, we can give time module.this is also build in python, we have just import and call.