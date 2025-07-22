from twilio.rest import Client

account_sid = 'ACdbd413a27be1a8c0d17af99d0fda3267'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16205018145',
  body='fire may occur',
  to='+919092362701'
)

print(message.sid)
