from dependencies.setting import driver,wait,hubbler_url,time
from social.channel.common_elements_for_channel import Interest_Channel,channel_listing_page
from dependencies.login import test_login_method

# Channel is created with all data
def test_create_channel():
    driver.maximize_window()
    print("entered channel listing")
    driver.get(channel_listing_page)
    channel = Interest_Channel()
    time.sleep(2)
    channel.find_channel_button().click()
    print("finding the element")
    channel.enter_channel_name().send_keys("Test Channel")
    channel.channel_description().send_keys("Channel Description")
    print("before profile pic")
    time.sleep(5)
    channel.channel_profile_picture().send_keys("/Users/hubbler1/Desktop/IMG_1557.JPG")
    print("after profile pic")
    print("before cover pic")
    time.sleep(2)
    channel.channel_cover_picture().send_keys("/Users/hubbler1/Desktop/IMG_1557.JPG")
    time.sleep(5)
    channel.channel_add_tag().click()
    channel.channel_add_tag().send_keys("Newtag")
    print("add tag")
    time.sleep(2)
    print("select tag")
    channel.channel_select_existing_tag().click()
    print("tag selected")
    time.sleep(2)
    channel.channel_create_button().click()


def test_delete_channel():
    channel = Interest_Channel()
    channel.edit_button().click()
    channel.delete_channel().click()
    channel.delete_pop_up_ok().click()


if __name__ == '__main__':
    test_login_method()
    test_create_channel()
    test_delete_channel()
