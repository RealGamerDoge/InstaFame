from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

accountPage = input("What is your account name: @")
hashtagPage = input("What is the hashtag name: #") 


driverPath = ""
driver = webdriver.Chrome(driverPath)

def enterUsername():
	userDriverSearch = driver.find_element_by_name("username") 
	if userDriverSearch == True:
		print("[INFO] Username box found!")
		userDriverSearch.send_keys(accountPage)
		userDriverSearch.send_keys(Keys.RETURN)

		sleep(10)
	else:
		try:
			userDriverSearch = driver.find_element_by_name("username")
			userDriverSearch.send_keys(accountPage)
		except IndexError:
			print("[INFO] Username box not found!")
			sleep(1000)
			print("Ending script...")
			quit()

enterUsername()



driver.get("https://instagram.com")

