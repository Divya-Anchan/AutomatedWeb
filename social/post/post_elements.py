from dependencies.setting import driver,wait
from dependencies.login import test_login_method
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

post_listing="https://sandapps.hubblerapp.com/web/social/feeds"


class Post_elements():

    def write_something_post(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='text-area']")))
    def enterpost_text(self):
        return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//textarea[@placeholder='Write something awesome!']")))
    def post_button(self):
        return wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "post-btn"))).click()
    def find_post(self):
        return  wait.until((EC.element_to_be_clickable((By.XPATH,"//div[@class"))))