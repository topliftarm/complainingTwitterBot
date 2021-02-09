from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "Your Email"
TWITTER_PW = "Your Password"

driver_path = "Your driver path"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0


#Get Internet Speed
    def get_internet_speed(self):
            self.driver.get("https://www.speedtest.net")
            go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
            go_button.click()
            time.sleep(60)
            self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
            print(self.down.text)
            self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
            print(self.up.text)

    def tweet_at_provider(self):
            self.driver.get("https://twitter.com/login")
            time.sleep(2)
            #login
            username = self.driver.find_element_by_name("session[username_or_email]")
            username.send_keys(TWITTER_EMAIL)
            password = self.driver.find_element_by_name("session[password]")
            password.send_keys(TWITTER_PW)
            time.sleep(2)
            password.send_keys(Keys.ENTER)
            time.sleep(5)
            #compose tweet
            compose_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
            compose_tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up, when my promised speed is {PROMISED_UP}up/{PROMISED_DOWN}down")
            time.sleep(2)
            send_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span')
            send_tweet.click()

bot = InternetSpeedTwitterBot(driver_path)
a = bot.get_internet_speed()
b = bot.tweet_at_provider()
