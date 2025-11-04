from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from time import sleep

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

# Save login session (optional)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)


# Add your credentials at the top of your script
ACCOUNT_EMAIL = "olaskeet@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "Zainab321*"      # The password you used during registration
ACCOUNT_NAME = "OLAHAMMED"
GYM_URL = "https://appbrewery.github.io/gym/"

WORKOUT_TYPE = "Spin Class"     # e.g., "Cardio", "Leg Day", "Yoga"
WORKOUT_TIME = "8:00 AM"         # e.g., "6am", "12pm", "6pm"

# Alternative to using time.sleep(): use a standalone wait object
wait = WebDriverWait(driver, 2)

# ---------------- LOGIN FUNCTIONS ---------------- #
def click_login_button():
    """Click the login button on the homepage."""
    login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

def login(email, password):
    """Fill and submit the login form."""
    try:
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = driver.find_element(By.NAME, "password")

        email_input.clear()
        email_input.send_keys(email)
        password_input.clear()
        password_input.send_keys(password)

        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()

        print("✅ Logged in successfully.")
    except TimeoutException:
        print("❌ Login fields not found. Page structure may have changed.")

def click_register():
    register_link = driver.find_element(By.CLASS_NAME, value="Login_toggleButton___tVY8")
    register_link.click()


def register():
    acct_name = driver.find_element(By.CLASS_NAME, value="Login_input__RLJo3")
    email = driver.find_element(By.NAME, value="email")
    password = driver.find_element(By.NAME, value="password")
    acct_name.send_keys(ACCOUNT_NAME)
    email.send_keys(ACCOUNT_EMAIL)
    password.send_keys(ACCOUNT_PASSWORD)
    register_click = driver.find_element(By.CLASS_NAME, value="Login_submitButton__tJFna")
    register_click.click()

all_schedule = []

# ---------------- WORKOUT BOOKING ---------------- #
def book_workout(workout_type, workout_time):
    """Select a workout and time slot, then confirm booking."""
    try:
        # Wait until the schedule page loads
        wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
        print("🏋️‍♀️ Schedule page loaded.")

        # Locate the workout section
        workouts = driver.find_elements(By.CSS_SELECTOR, ".ClassCard_card__KpCx5")
        selected = None

        for workout in workouts:
            print(workout)
            print("########")
            title = workout.find_element(By.CLASS_NAME, "ClassCard_className__q0kVz").text
            print(title)
            if workout_type.lower() in title.lower():
                selected = workout
                break

        if not selected:
            print(f"⚠️ Workout '{workout_type}' not found.")
            return

        # Find time slots within that workout
        time_slots = selected.find_elements(By.CSS_SELECTOR, "p[id^='class-time-']")
        # print(time_slots.text)
        slot_selected = False
        for slot in time_slots:
            slot_text = slot.text.strip().lower()
            if workout_time.lower() in slot_text:
                slot.click()
                print(f"🕕 Selected {workout_type} at {workout_time.upper()}.")
                slot_selected = True

                break

        if not slot_selected:
            print(f"⚠️ Time slot '{workout_time}' not available.")
            return

        # Confirm booking
        confirm_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#book-button-spin-2025-11-05-0800")))
        confirm_btn.click()
        print("✅ Booking confirmed successfully!")

    except TimeoutException:
        print("❌ Booking page elements not found. Check structure or wait time.")



def spool_schedule():
    schedules = driver.find_elements(By.CSS_SELECTOR, value=".ClassCard_card__KpCx5")
    for _ in schedules:
        print(_.text)
        # time_lines = driver.find_elements(By.CSS_SELECTOR, value="ClassCard_classDetail__Z8Z8f")
        # all_schedule.append(time_lines)
    return

driver.get(GYM_URL)
click_login_button()
# click_register()
login(ACCOUNT_EMAIL, ACCOUNT_PASSWORD)
# register()
# sleep(1)
# click_register()
sleep(3)
# register()
# login(ACCOUNT_EMAIL, ACCOUNT_PASSWORD)
# spool_schedule()
# print(all_schedule)
sleep(5)
book_workout(WORKOUT_TYPE, WORKOUT_TIME)
# wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# login(ACCOUNT_EMAIL, ACCOUNT_PASSWORD)
# driver.quit()

