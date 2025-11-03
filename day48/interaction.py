from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

total_interactions = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')

print(total_interactions.text)


driver.quit()