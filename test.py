from twilio.rest import Client

# Twilio credentials
account_sid = "ACd4052c916008626174e5017a3570fd5b"
auth_token = "fd05eb12160ffacaa68278831b440c67"
from_number = "+18155154790"  # Your Twilio number
to_number = "+917876568316"   # Your verified number

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Test message from Twilio trial account 🚀",
    from_=from_number,
    to=to_number
)

print("Message SID:", message.sid)
