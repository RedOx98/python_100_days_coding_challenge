from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
speed_url = "https://www.speedtest.net/"

SPEED_URL = "https://www.speedtest.net/"

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "olaskeet@gmail.com"
TWITTER_PASSWORD = "12345675"
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        wait = WebDriverWait(self.driver, 5)
        self.driver.get(SPEED_URL)
        sleep(5)
        ok_page = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        ok_page.click()
        sleep(3)
        go_button = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')
        go_button.click()
        sleep(15)
        # cancel_button = wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Back to test results")))
        # cancel_button = self.driver.find_element(By.LINK_TEXT, "Back to test results")
        # cancel_button.click()
        time.sleep(60)
        self.up = self.driver.find_element(By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

        return download_speed

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element(By.XPATH,
                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH,
                                            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()