from twilio.rest import Client as TwilioClient
from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM, MY_PHONE

class NotificationManager:
    def __init__(self):
        self.client = TwilioClient(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        msg = self.client.messages.create(
            body=message,
            from_=TWILIO_FROM,
            to=MY_PHONE
        )
        print("SMS sent:", msg.sid)