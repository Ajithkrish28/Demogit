'''
Chrome Options

it is how to behave chrome
selenium didn't know how to handle chrome its handle only webpage HTML
so, we define how to handle chrome

these all behave in ChromeOption class
we create an object of ChromeOption class
and e have give behave in " ".

'''
import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")        #- first we do chrom invoke and maximize but in this behave first maximize window then invoke
#chrome_options.add_argument("headless")          # - headless is we can't see in visually , it's work background
chrome_options.add_argument("--ignore-certified-errors")   # it's ignore all certified errors

'''
before we define how behave chrome but chrome didn't know
so, we pass that
behaviour is object, that object pass in invoke chrome
'''
driver = webdriver.Chrome(options=chrome_options)  # actually it's chrome invoke
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")