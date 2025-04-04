'''
child window handle( one tab to another tab )

selenium is can't access directly to another tab

so, we use switch

# once we switch parent to child selenium do in only child window not parent if we want parent window access we again switch child to parent

'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(3)   # some time page loaded get time

# we need give child tab name, so we use windows handles
# it's return a list window name and store a index order from 0
# selenium in tab(parent) that tab is 0 next tabs are saved next index order
name = driver.window_handles

# we switch the window from parent to child, we, use switch_to
# selenium didn't know which tab to switch, so that recession we give tab name
# we already save tab name in index order.in this cause we give 1st index
driver.switch_to.window(name[1])

'''we use TAG_ NAME, it's also like ID, NAME, CLASS_NAME, (it's we give unique tag name )'''

child_window = driver.find_element(By.TAG_NAME, "h3").text
print(child_window)
driver.close()   # it's used to close the current window(tab)

# we again switch child to parent
# we already save windows name, we give windows tab name with order index
driver.switch_to.window(name[0])
time.sleep(3)
parent_window = driver.find_element(By.XPATH, "//div/h3").text
print(parent_window)


