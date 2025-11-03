import smtplib
import random
import datetime as dt

# with smtplib.SMTP("smtp.gmail.com") as connection: # gmail: smtp.gmail.com, live: smtp.live.com, hotmail: smtp.mail.yahoo.com
#     connection.starttls()
#     connection.login(my_email, my_password)
#     connection.sendmail("olaskeet@gmail.com", "olaskeet123@gmail.com", "Hello\n\n, this is the body of my mail for this pythonista")
#     connection.close()

MY_EMAIL = "olaskeet@gmail.com"
MY_PASSWORD = "snvjgxxtriwyaion"
TO_EMAIL = "olaskeet123@gmail.com"
now = dt.datetime.now()
year = now.year
weekday = now.weekday()
print(year)

with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)
    print(quote)

if weekday == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Monday Motivation 💪\n\n{quote}"
        )
    print("Motivational email sent successfully!")
else:
    print("Today is not Monday, skipping email.")