# Download selenium for python
# Download webdriver for Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# create a new Chrome browser instance
browser = webdriver.Chrome()

# navigate to the Google search page
browser.get('https://www.google.com/')

time.sleep(3)

reject_button = browser.find_element("xpath", '//*[@id="W0wltc"]/div')
reject_button.click()

time.sleep(3)

# find the search box element and enter the search term
search_box = browser.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys('hello world')

time.sleep(3)

# submit the search query
search_box.submit()

# close the browser
# browser.quit() 
