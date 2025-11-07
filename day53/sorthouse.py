import requests
from bs4 import BeautifulSoup
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# ⚙️ Setup Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class SortHousing:
    def __init__(self):
        self.sf_google_form_url = "https://forms.gle/uj62xPT7qViPXej69"
        self.zillow_url = "https://appbrewery.github.io/Zillow-Clone/"
        # self.pd = Pandas()
        self.apartments = []
        self.google_sheet_url = "https://api.sheety.co/cfe410972db5adc5401fb03798265f66/sfRentingResearch/formResponses1"
        self.GOOGLE_FORM_URL = "https://forms.gle/RYssr1BmSUqNEipX8"
        self.driver = webdriver.Chrome( options=chrome_options)


    def fetch_sf_house(self):

        response = requests.get(self.zillow_url)
        home_pg = response.text
        soup = BeautifulSoup(home_pg,"html.parser")


        aptmt_prices = [price.get_text().split("+")[0] for price in soup.select(".PropertyCardWrapper__StyledPriceLine")]
        aptmt_address = [address.get_text().strip() for address in soup.select("address")]
        aptmt_links = [link["href"] for link in soup.select(".List-c11n-8-84-3-photo-cards a")]



        for n in range(len(aptmt_prices)):
            self.apartments.append({
                "address": aptmt_address[n],
                "price": aptmt_prices[n],
                "link": aptmt_links[n]
            })

        print(self.apartments)

    def form_filler(self):


        for property in self.apartments:
            self.driver.get(self.GOOGLE_FORM_URL)
            sleep(2)

            # Adjust the XPaths below to match your form fields
            address_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

            address_input.send_keys(property["address"])
            price_input.send_keys(property["price"])
            link_input.send_keys(property["link"])

            submit_button.click()
            sleep(2)
            print("✅ All data submitted successfully!")
        self.driver.quit()
