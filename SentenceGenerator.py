from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import time

def click_button(xpath):
	time.sleep(.5) 										# Let the page load
	button_to_click = driver.find_element_by_xpath(xpath)
	button_to_click.click()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.thewordfinder.com/random-sentence-generator/')
time.sleep(1)

click_button('//*[@id="accept-choices"]') 					            	# Accept cookies / consent
click_button('//*[@id="adj_sentences"]')					            	# No questions
click_button('//*[@id="subset-short"]')						            	# Short sentences only
search_box = driver.find_element_by_xpath('//*[@id="sentence_count"]')
search_box.send_keys('20')									# Generate maximum no. of sentences
search_box.submit()										# Enter
sentences = []
for i in range(500):
	click_button('//*[@id="copyGeneratedSentences"]')		            		# Copy Sentences
	sentencesGen = pyperclip.paste().splitlines()					    	# Using pyperclip, paste sentences to a list
	sentences.extend(sentencesGen)
	driver.refresh()

print(str(sentences[1]) + " < 1")

[x for x in sentences if x.strip()]								# Remove whitespace
sentences = list(dict.fromkeys(sentences))						        # Remove duplicates

with open('GenerartedSentences.txt','w') as file:			            		# Open/Create file called generated sentences
	for sentence in sentences:
		file.write(sentence + '\n')

print('success')
driver.quit()										
