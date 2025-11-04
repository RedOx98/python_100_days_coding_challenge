from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://python.org")

# total_interactions = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# total_interactions = driver.find_element(By.CSS_SELECTOR, value='#articlecount ul li a')
# total_interactions = driver.find_element(By.LINK_TEXT, value="Content portals")
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
# search.send_keys(Keys.ENTER)
# total_interactions.click()
# articlecount
print(total_interactions.text)


driver.quit()