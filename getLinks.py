from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

instagramUsername = ""

accountPage = "https://instagram.com/" + instagramUsername

driverPath = ""
driver = webdriver.Chrome(driverPath)

def getInstagramPage():
	driver.get(accountPage)
