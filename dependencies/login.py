from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from dependencies.setting import driver,wait,hubbler_url


def test_login_method():
    print("in login start")
    driver.get(hubbler_url)
    Login_with_OTP = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Login With OTP')]")))
    Login_with_OTP.click()
    # To enter Number
    Number = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='mobile/ email']")))
    Number.send_keys("9731771947")
    time.sleep(2)
    # tO CLICK ON NEXT
    Next = wait.until(EC.element_to_be_clickable((By.ID, "otpNext")))
    Next.click()
    # to enter otp value
    OTP = wait.until(EC.element_to_be_clickable((By.ID, "optNumber")))
    OTP.send_keys("122221")
    time.sleep(5)
    print("in login end")

#
# test_login_method()


if __name__ == '__main__':

    test_login_method()
