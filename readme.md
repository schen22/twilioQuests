1. donwload ngrok: https://dashboard.ngrok.com/get-started
2. attach authtoken
3. ~/.ngrok http 5000

`$ pip install twilio`

`$ export FLASK_APP=twilio.py`

`$ flask run`
  - defaults to port 5000

navigate to ngrok generated url upon appending uri `/inbound`

Go to twilio numbers and update settings for the phone number twilio gave to accept this webhook from the ngrok generated url. https://www.twilio.com/console/phone-numbers Messaging section.

![twilio](/photos/twilioMessaging.png)

Text the number, and receive the xml defined message.

![message](/photos/sentMessage.png)
