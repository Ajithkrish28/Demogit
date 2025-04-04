from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximize")


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

driver.find_element(By.CSS_SELECTOR, "#downloadButton").click()

# update the Excel file here




# we save that web element(locator) in variable and send to the file location, we use send keys
# if we upload a file locator attribute wil be in type=file it's mandatory

upload_file = driver.find_element(By.CSS_SELECTOR, "input[type='file']")  # don't click,if click will open this pc, selenium can't access
upload_file.send_keys()   # pass file location



'''this code get the error because we didn't give file location'''