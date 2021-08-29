from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

desktop_driver_path = "C:/Users/user/PycharmProjects/chromedriver.exe"
SIMILAR_ACCOUNT = "canonhongkong"
IG_USERNAME = os.environ["IG_EMAIL"]
IG_PASSWORD = os.environ["IG_PASSWORD"]


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=desktop_driver_path)


    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        # switch_account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/button[1]')
        # switch_account.click()
        # time.sleep(1)
        user_name = self.driver.find_element_by_name("username")
        user_name.send_keys(IG_USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(IG_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        turn_on_notifications = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]')
        turn_on_notifications.click()
        time.sleep(2)


    def find_follower(self):
        search_account = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_account.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        search_account.send_keys(Keys.ENTER)
        search_account.send_keys(Keys.ENTER)
        time.sleep(2)
        followers_tab = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers_tab.click()
        time.sleep(2)

    def follow(self):
        # last_height = self.driver.execute_script("return document.body.scrollHeight")
        # while True:
        #     # Scroll down to bottom
        #     self.driver.execute_script('document.getElementByClassName("Pzuss").scrollTo(0, document.body.scrollHeight);')
        #
        #     # Wait to load page
        #     time.sleep(1)
        #
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

        # time.sleep(1)
        scroll_count = 0
        scroll_box = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul')
        follow_btn = self.driver.find_elements_by_css_selector("li div button")
        for follow in follow_btn:
            follow.click()
            scroll_count += 1
            time.sleep(1)
            if scroll_count % 6 == 0:
                scroll_box.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)



auto_follower = InstaFollower()
auto_follower.login()
auto_follower.find_follower()
auto_follower.follow()
