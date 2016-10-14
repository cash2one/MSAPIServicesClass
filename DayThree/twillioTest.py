from twilio.rest import TwilioRestClient

account_sid = "AC655946350eb5225949fa77056c684754"
auth_token = "d931383f9b141d37de0a0844669f3796"

client = TwilioRestClient(account_sid, auth_token)


message = client.messages.create(
    to="+14083688346",
    from_="+16697219848",
    body="Hello there!"
)
