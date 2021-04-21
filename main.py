from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from login import loginToInstagram

from getLinks import getInstagramPage


driverPath = ""
driver = webdriver.Chrome(driverPath)

sleep(1)

loginToInstagram()
getInstagramPage()
