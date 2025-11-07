from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import os

# path to chromedriver if needed
CHROMEDRIVER_PATH = "chromedriver"  # or full path

# build file URL
html_path = os.path.abspath("http://www.tinder.com")
file_url = f"file:///{html_path}"

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=ChromeService(CHROMEDRIVER_PATH), options=options)
driver.get(file_url)
time.sleep(1)  # wait for page to load

actions_log = []

def top_card():
    try:
        return driver.find_element(By.CSS_SELECTOR, "#deck .card")
    except NoSuchElementException:
        return None

def decide_and_swipe(card_element):
    # read profile text
    name = card_element.find_element(By.CSS_SELECTOR, ".name").text
    bio = card_element.find_element(By.CSS_SELECTOR, ".bio").text
    print(f"Deciding for profile: {name} | {bio}")

    # example heuristics (customise as you like)
    # - like if bio contains 'engineer' or 'data' or 'python'
    # - like if age between 24 and 32
    decision = "nope"
    lower_bio = bio.lower()
    if any(k in lower_bio for k in ("engineer","devops","data","python","frontend","backend")):
        decision = "like"
    else:
        # basic age check from name field (e.g., "Aisha, 28")
        try:
            age_part = name.split(",")[-1].strip()
            age = int(age_part)
            if 24 <= age <= 32:
                decision = "like"
        except:
            pass

    # click appropriate button
    if decision == "like":
        btn = card_element.find_element(By.CSS_SELECTOR, "button.like")
    else:
        btn = card_element.find_element(By.CSS_SELECTOR, "button.nope")
    btn.click()
    actions_log.append({"profile": name, "decision": decision})
    print(f"-> {decision.upper()}")

# Main loop: iterate until no cards remain
while True:
    c = top_card()
    if not c:
        print("No more profiles.")
        break
    decide_and_swipe(c)
    time.sleep(0.8)  # pace between swipes

print("Actions log:", actions_log)
driver.quit()