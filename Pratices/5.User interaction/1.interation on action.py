'''in this lecture mouse action'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

'''
just mouse working we see
mouse working is import from selenium ( ActionChains )
mouse working are:
1.move_to_element()- it's just go to element not do any work or perform and it also work click(), which element to move that element locator we give
2.context_click() - perform right chick, which element do right click that element locator we can give 
3.double_click() - it's do double click
4.click_and_hold() - it's just go to element and hold not click
5.drag_and_drop(locator 1, locator 2)  - click and drag and move some where element  ,  (we give which element we drag that element locator we give(locator 1), which locator we past that element locator(locator 2) ) 


perform ()  -  we give any action, it's mandatory end with perform()
'''

'''
# move_to_element and context_click

# we create object of ActionChains class and pass driver parameter. ( driver is global )
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
'''

action = ActionChains(driver)
action.double_click(driver.find_element(By.XPATH, "//div[@id='checkbox-example']/fieldset/label/input[@id='checkBoxOption2']")).perform()