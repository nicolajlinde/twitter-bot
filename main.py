import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import speedtest
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("TWITTER_EMAIL")
PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        driver_path = "C:/Users/nicol/Documents/Development/chromedriver.exe"
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.st = speedtest.Speedtest()

    def get_speedtest(self):
        print("Fetching speeds..")
        download = round(self.st.download() / 1000000, 2)
        upload = round(self.st.upload() / 1000000, 2)
        return [download, upload]

    def login(self):
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        login = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        login.click()

        time.sleep(2)

        input_email = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        input_email.clear()
        input_email.send_keys(EMAIL)

        time.sleep(1)

        next_btn = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_btn.click()

        time.sleep(2)

        input_username = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        input_username.send_keys("NicoAltAccount")

        next_btn = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        next_btn.click()

        time.sleep(2)

        input_password = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        input_password.clear()
        input_password.send_keys(PASSWORD)

        time.sleep(2)

        login_btn = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_btn.click()

    def tweet_at_provider(self, down, up):
        self.login()
        time.sleep(2)
        input_tweet = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        input_tweet.send_keys(f"My internet speed is: {down}mbps/{up}mbps")
        time.sleep(2)
        tweet_btn = self.driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()


bot = InternetSpeedTwitterBot()
data = bot.get_speedtest()
bot.tweet_at_provider(data[0], data[1])
