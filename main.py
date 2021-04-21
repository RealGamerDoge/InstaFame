from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from login import loginToInstagram

from getLinks import getInstagramPage


driverPath = "C:/Users/youss/Downloads/chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(driverPath)

sleep(1)

loginToInstagram()
getInstagramPage()
