'''
handling JavaScript in selenium python

in webpage developed based on Javascript
what work do Javascript that work selenium can't do, selenium just help,
(like scroll down ) , selenium can't do scroll

'''
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

# change driver to Javascript mode,
# use .execute_async_script() , Javascript executed in execute_async_script

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")   # window-current page, number(0,500) - pic-sell (scroll 0 pic-sell to 500 pic-sell)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")  # top to bottom


# driver.get_screenshot_as_file("scree.png")  # it's take screen shoot.screen - we give image store file name

time.sleep(3)
