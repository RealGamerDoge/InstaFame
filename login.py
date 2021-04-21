from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

instagramUsername = ""
instagramPassword = ""


accountPage = "https://instagram.com/" + instagramUsername

driverPath = ""
driver = webdriver.Chrome(driverPath)


def loginToInstagram:
	driver.get("https://www.instagram.com/accounts/login/")
	sleep(1)

	enterUser = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
	enterPass = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

	loginButton = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

	enterUser.send_keys(instagramUsername)
	enterUser.send_keys(Keys.RETURN)

	enterPass.send_keys(instagramPassword)
	enterPass.send_keys(Keys.RETURN)

	loginButton.click()

	sleep(4)

driver.get(accountPage)
