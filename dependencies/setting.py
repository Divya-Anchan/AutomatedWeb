import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotSelectableException, NoSuchElementException, \
    ElementNotVisibleException, TimeoutException

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("/Users/hubbler1/PycharmProjects/SeleniumLocatorsPractice/driver/chromedriver 4")

wait = WebDriverWait(driver, 20, poll_frequency=1,
                     ignored_exceptions=[ElementNotSelectableException, ElementNotVisibleException,
                                         NoSuchElementException, TimeoutException])
hubbler_url = "https://sandconsole.hubblerapp.com"

# time= time.sleep(3)
# quit=driver.quit()
# close=driver.close()