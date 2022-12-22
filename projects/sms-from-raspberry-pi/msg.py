from twilio.rest import Client

account_sid = "your sid"
account_token = "your access token"
client = Client(account_sid, account_token)

message = client.messages.create(
        body='Hello From Raspberry Pi',
        from_= '+13042444362',
        to='receivers_number'
    )

print(message.sid)
