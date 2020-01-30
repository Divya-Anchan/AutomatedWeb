from dependencies.setting import wait,driver
from social.post.post_elements import Post_elements,post_listing
from dependencies.login import test_login_method


def test_post():
    driver.get(post_listing)
    post = Post_elements
    Post_elements.write_something_post().click()
    Post_elements.enterpost_text().send_keys("New Post")
    Post_elements.post_button().click()


if __name__ == '__main__':

  test_login_method()
  test_post()



