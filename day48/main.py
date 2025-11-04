from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://iunion.unionbankng.com:8443/ords/f?p=110:LOGIN:14378948128862:::::")
# driver.get("https://python.org")
username = "carexpress_f90vr"
password = "Hasbeeyah19*"

# union_name = driver.find_element(By.XPATH, value='//*[@id="R276374988374023328"]/p[1]')
# print(union_name.text)
# upcoming_events_time = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
# upcoming_events_name = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
# # print(upcoming_events)
# events = {}
# for n in range(len(upcoming_events_time)):
#     events[n] = {
#         "time": upcoming_events_time[n].text,
#         "event": upcoming_events_name[n].text
#     }

# print(events)
user_input = driver.find_element(By.ID, "P9999_USERNAME")
user_password = driver.find_element(By.ID, "P9999_PASSWORD")
login = driver.find_element(By.XPATH, value='//*[@id="lgbtn"]/span')
# breadcrumb = driver.find_element(By.XPATH, value='//*[@id="t_Button_navControl"]')
# carecube_tab = driver.find_element(By.XPATH, value='//*[@id="t_TreeNav_1"]/span')
user_input.send_keys(username)
user_password.send_keys(password)
login.click()
# breadcrumb.click()
# carecube_tab.click()
# print(f"username: {user_input.get_attribute("name")} and password: {user_password.get_attribute("name")}")
#
# # bus_link = driver.find_element(By.CSS_SELECTOR, "fa-bus a")
# # print(bus_link.text)
# # //*[@id="t_TreeNav_4"]/div[2]/a
#
#
# # driver.close()
# driver.quit()
# # print("abc")
# # //*[@id="R276374988374023328"]/p[1]