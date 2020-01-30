# for deleting text
from selenium.webdriver.common.keys import Keys


def delete_text(element):
    for i in range(len(element.get_attribute("value"))):
        element.send_keys(Keys.BACK_SPACE)


# My day listing page





# channel listing page

channel_listing_page = "https://sandapps.hubblerapp.com/web/social/channels"

# event listing page
event_listing_page = "https://sandapps.hubblerapp.com/web/social/events"


# group listing page

group_listing_page = "https://sandapps.hubblerapp.com/web/social/groups"

# poll listing page
poll_listing_page = "https://sandapps.hubblerapp.com/web/social/polls"