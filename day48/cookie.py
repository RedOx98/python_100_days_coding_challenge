from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

# Wait for page to load just in case
sleep(5)

# Handle initial popups (cookies consent does not have to be clicked, but language does)
print("Looking for language selection...")
try:
    # Select English language
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3) # more loading
except NoSuchElementException:
    print("Language selection not found")


# ------------------ SELECTORS ------------------ #
cookie = driver.find_element(By.ID, "bigCookie")

# Store item IDs (for upgrades)
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time() + 5  # Every 5 seconds, check for upgrades
five_min = time() + 60*5  # Stop after 5 minutes

# english = driver.find_element(By.CLASS_NAME, value='langSelectButton')
# print(english.text)

# ------------------ MAIN LOOP ------------------ #
while True:
    cookie.click()

    # Every 5 seconds, check upgrades
    if time() > timeout:
        # Get all upgrade prices
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in all_prices:
            text = price.text
            if text != "":
                cost = int(text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current money
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        # Find upgrades affordable
        affordable_upgrades = {cost: id for cost, id in cookie_upgrades.items() if money > cost}

        # Purchase the most expensive affordable upgrade
        if affordable_upgrades:
            highest_price = max(affordable_upgrades)
            driver.find_element(By.ID, affordable_upgrades[highest_price]).click()

        timeout = time.time() + 5  # Reset 5-second timer

    # Stop after 5 minutes
    if time() > five_min:
        cookies_per_s = driver.find_element(By.ID, "cps").text
        print(f"🍪 Cookies per second: {cookies_per_s}")
        break



# //*[@id="bigCookie"]