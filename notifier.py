from twilio.rest import Client
import os

class Notifier:
    def __init__(self):
        self.client = Client(os.getenv('TWILIO_ACCOUNT_SID'), os.getenv('TWILIO_AUTH_TOKEN'))
        self.from_phone = os.getenv('TWILIO_FROM_NUMBER')
        self.to_phone = os.getenv('USER_PHONE_NUMBER')

    async def send(self, message):
        try:
            self.client.messages.create(
                body=message,
                from_=self.from_phone,
                to=self.to_phone
            )
            print(f"[SMS SENT] {message}")
        except Exception as e:
            print(f"[ERROR] Failed to send SMS: {e}")