'''
Headless

normally we run in chrome it's visible, but we choose headless it's run in background, but we can't see visibly

'''

import time
from selenium import webdriver


# we create object of ChromeOption class
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")   # we access add_argument and pass "headless"


chrome_option.add_argument("--ignore-certified-errors") # - it's use for ignore certified error like page can't login, not connected

# normally we create object of Chrome class
# we pass parameter of option= and give headless object

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(3)