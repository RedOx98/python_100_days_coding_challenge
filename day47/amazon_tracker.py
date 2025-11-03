import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}

# ------------------ SCRAPE AMAZON ------------------ #
URL = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ?th=1"
response = requests.get(URL)
TARGET_PRICE = 800.00  # 👈 Your target price

price_wp = response.text
soup=BeautifulSoup(price_wp, "lxml")

# Extract product title
title = soup.find(id="productTitle").get_text(strip=True)

# Extract price (can vary by country)
price_str = soup.find(class_="a-price-whole").get_text(strip=True).replace(",", "").split(".")[0]
price_fraction = soup.find(class_="a-price-fraction").get_text(strip=True)
# print(price_str)
price = float(f"{price_str}.{price_fraction}")

print(f"Product: {title}")
print(f"Current Price: ${price}")

# ------------------ ALERT CONDITION ------------------ #
if price <= TARGET_PRICE:
    print("✅ Price dropped! Sending email alert...")

    # ------------------ EMAIL CONFIG ------------------ #
    sender_email = "<noreply>@gmail.com"
    receiver_email = "olaskeet@gmail.com"
    app_password = "snvjgxxtriwyaion"  # Use app password if 2FA is on

    subject = "🔥 Amazon Price Drop Alert!"
    body = f"{title} is now ${price}!\n\nCheck it out here: {URL}"

    # Create message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(sender_email, app_password)
        connection.send_message(msg)

    print("📨 Email sent successfully!")
else:
    print("No price drop yet. Keep watching.")