'''
Frame handle
frame is  embedded HTML, it's look like HTML but not.it's called frame
webdriver was can't direct access to frame, driver not knowledge for access frame
so, we change method to frame method
we use driver.switch_to.frame()
'''



import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()

# driver change to frame 
driver.switch_to.frame("mce_0_ifr")    # pass parameter is ID or NAME values
print(driver.find_element(By.CSS_SELECTOR, "#tinymce").text)


# frame to default driver
#  in frame it's can't access to original page so we change

driver.switch_to.default_content()     # now we not give any parameters
print(driver.find_element(By.XPATH, "//div/p").text)
time.sleep(3)
