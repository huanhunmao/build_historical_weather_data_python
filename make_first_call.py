# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

# 失败了 因为 不能向国内打
account_sid = "xx"
auth_token = "xxx"
client = Client(account_sid, auth_token)

call = client.calls.create(
  url="http://demo.twilio.com/docs/voice.xml",
  to="+861xxxx",
  from_="+17xxx"
)

print(call.sid)