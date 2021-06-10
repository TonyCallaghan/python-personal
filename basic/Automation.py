from selenium import webdriver
import time
from datetime import date

print("**********************")
print("Enter receipt number: ")
receipt = input('e.g 1234/123/123/123/123: ')
print("**********************")
receipt_numbers = receipt.split('/')

paths = ['//*[@id="L2AGLb"]/div', #0
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', #1
'//*[@id="rso"]/div[1]/div/div/div[1]/a/div/cite', #2
'//*[@id="im_policy_accept_button"]/span', #3
'//*[@id="promptInput_216804"]','', #4/5
'//*[@id="prompt_444844"]/div[2]/div/div[1]/div[1]', #6
'//*[@id="prompt_444845"]/div[2]/div/div[1]/div[5]', #7
'//*[@id="prompt_444847"]/div[2]/div/div[1]/div[1]', #8
'//*[@id="prompt_472436"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #9
'//*[@id="prompt_137397"]/div[2]/div/div[1]/div/div/div[11]/label/div/div', #10
'//*[@id="promptInput_183852"]', #11 //*[@id="promptInput_183852"]
'//*[@id="prompt_137415"]/div[2]/div/div[1]/div[2]/label', #12
'//*[@id="prompt_137421"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #13
'//*[@id="prompt_137426"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #14
'//*[@id="prompt_377367"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #15
'//*[@id="prompt_377368"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #16
'//*[@id="prompt_377369"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #17
'//*[@id="prompt_377370"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #18
'//*[@id="prompt_377371"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #19
'//*[@id="prompt_137434"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #20
'//*[@id="prompt_377372"]/div[2]/div/div[1]/div/div/div[5]/label/div/div', #21
'//*[@id="prompt_377373"]/div[2]/div/div[1]/div[1]', #22
'//*[@id="prompt_137442"]/div[2]/div/div[1]/div[1]', #23
'//*[@id="prompt_432939"]/div[2]/div/div[1]/div[1]', #24
'//*[@id="commentArea_137857"]', #25
'//*[@id="prompt_137422"]/div[2]/div/div[1]/div[2]', #26
'//*[@id="prompt_137411"]/div[2]/div/div[1]/div[6]', #27 
'//*[@id="prompt_137409"]/div[2]/div/div[1]/div[2]', #28
'//*[@id="prompt_158931"]/div[2]/div/div[1]/div[2]', #29
'//*[@id="prompt_410150"]/div[2]/div/div[1]/div[2]', #30
'//*[@id="prompt_137406"]/div[2]/div/div[1]/div[2]', #31
'//*[@id="prompt_185955"]/div[2]/div/div[1]/div[2]' #32
]

def click_button(xpath):
	time.sleep(1.1) # Let the page load
	button_to_click = driver.find_element_by_xpath(xpath)
	button_to_click.click()

def next_page():
	time.sleep(1.5)
	click_button('//*[@id="nextPageLink"]')

def enter_receipt():
	for i in range(0,5): # Fill in rec number
		if i == 4:
			text_box = driver.find_element_by_xpath(paths[4])
		else:
			text_box = driver.find_element_by_xpath('//*[@id="promptInput_358921_' +str(i)+'"]')
		text_box.send_keys(receipt_numbers[i])

def tick_boxes():
	next_page()
	next_page()
	click_button(paths[6])
	click_button(paths[7])
	click_button(paths[8])
	next_page()
	click_button(paths[9])
	next_page()
	next_page()
	click_button(paths[10])
	next_page()
	click_button(paths[11])
	box = driver.find_element_by_xpath(paths[11])
	box.send_keys(date.today().strftime("%d/%m/%Y"))
	click_button(paths[12])
	next_page()
	click_button(paths[13])
	click_button(paths[14])
	click_button(paths[15])
	click_button(paths[16])
	click_button(paths[17])
	click_button(paths[18])
	next_page()
	click_button(paths[19])
	click_button(paths[20])
	click_button(paths[21])
	click_button(paths[22])
	next_page()
	click_button(paths[23])
	next_page()
	click_button(paths[24])
	click_button(paths[25])
	box = driver.find_element_by_xpath(paths[25])
	box.send_keys("The guy on till 5 was very funny and chatty, it's rare to see a cashier so interactive with there customers. It really made my day.")
	next_page()
	click_button(paths[26])
	next_page()
	click_button(paths[27])
	click_button(paths[28])
	click_button(paths[29])
	next_page()
	click_button(paths[30])
	click_button(paths[31])
	next_page()
	click_button(paths[32])
	next_page()
	next_page()

driver = webdriver.Chrome()
driver.get('https://google.com')
click_button(paths[0]) # Accept Google consent

search_box = driver.find_element_by_xpath(paths[1])
search_box.send_keys('tellaldi ie')
search_box.submit()

click_button(paths[2]) # Go to Aldi survey section
time.sleep(1.5) # Let the page load
click_button(paths[3]) # Accept Aldi consent

enter_receipt()
tick_boxes()
driver.quit()

# cd desktop\Pyt 

# python Automation.py  5679/872/042/005/019
