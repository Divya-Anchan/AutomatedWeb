import time
import os
from selenium import webdriver
from selenium.common.exceptions import ElementNotSelectableException, NoSuchElementException, \
    ElementNotVisibleException, TimeoutException

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

path = os.path.dirname(os.path.abspath(__file__))+"/Driver/chromedriver 4"
driver = webdriver.Chrome("/Users/hubblerwork/PycharmProjects/AutomatedWeb/dependencies/Driver/chromedriver 4")

wait = WebDriverWait(driver, 20, poll_frequency=1,
                     ignored_exceptions=[ElementNotSelectableException, ElementNotVisibleException,
                                         NoSuchElementException, TimeoutException])
hubbler_url = "https://sandapps.hubblerapp.com"

Action=ActionChains(driver)

# time= time.sleep(3)
# quit=driver.quit()
# close=driver.close()