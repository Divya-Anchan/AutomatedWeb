from dependencies.setting import driver,wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# To enter the channel listing page
channel_listing_page = "https://sandapps.hubblerapp.com/web/social/channels"


class Interest_Channel:


    def find_channel_button(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='bt']")))

    def enter_channel_name(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Channel Name']")))

    def channel_description(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH,"//textarea[@placeholder='description']")))


    def channel_create_button(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='bt blue']")))

    def click_on_existing_channel(self):
        return wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='channel-list-container']//li[1]")))

    def edit_button(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='edit']")))

    def update_button(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Update')]")))

    def delete_channel(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='bt delete']")))

    def delete_pop_up_ok(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='popupHold popupDelete top65']//button[@class='bt ok-bt']")))

    def delete_pop_up_cancel(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='popupHold popupDelete top65']//button[@class='bt']")))


    def channel_profile_picture(self):
        return driver.find_element_by_css_selector("input#files1")

    def channel_cover_picture(self):
        return driver.find_element_by_css_selector("input#files")

    def channel_select_existing_tag(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='drop-down-body multi-select-type']//li[contains(text(),'Newtag')]")))

    def channel_add_tag(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder='Add tags']")))

    def channel_select_new_tag(self):
        return wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@class='list-item']")))

















