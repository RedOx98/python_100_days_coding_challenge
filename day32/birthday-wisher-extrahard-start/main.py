import pandas
import datetime as dt
import random
import smtplib
import pandas as pd

##################### Extra Hard Starting Project ######################
# Your email credentials
MY_EMAIL = "olaskeet@gmail.com"
MY_PASSWORD = "snvjgxxtriwyaion"

# 1️⃣ Read today's date
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# 2️⃣ Read the birthdays.csv file
data = pd.read_csv("birthdays.csv")

# Convert the DataFrame into a dictionary with tuple keys
birthdays_dict = {
    (row.month, row.day): row for (index, row) in data.iterrows()
}
# 3️⃣ Check if today matches a birthday in the file
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    name = birthday_person["name"]
    email = birthday_person["email"]

    # 4️⃣ Pick a random letter template
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", name)
        print(contents)

    # 5️⃣ Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday, {name}! 🎉\n\n{contents}"
        )
    print(f"🎈 Birthday email sent to {name} ({email}) successfully!")
else:
    print("No birthdays today.")






