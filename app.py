import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from dotenv import dotenv_values
config = dotenv_values(".env")


# driver = webdriver.Chrome(executable_path = 'driver/chromedriver_linux64/chromedriver')
# driver = webdriver.Edge(executable_path='driver/edgedriver_linux64/msedgedriver')

driver = webdriver.Firefox()


driver.get('http://superbuy.com.br/')
