#!/usr/bin/env python2
import httplib2
import json
import urllib
from twilio.rest import TwilioRestClient

GOOGLE_API_KEY = "AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk"
TRANSLATE_URL = "https://www.googleapis.com/language/translate/v2?key=AIzaSyC0XYY3AWKWKQlQbwm1mzI0-K4_CoFCCrk&source=en&target="
ACCOUNT_SID = "ACe52de0823ec698f8c793b393b51b9d65"
AUTH_TOKEN = "2bf65d5c10e520123278195ff3cddd4d"

text = ["Everything is Awesome", "Everything is cool when you are part of a team", "Teamwork makes the dreamwork", "This is the last string"]
translatedText1 = []


def googleTranslate(text, language):
    if type(text) == str:
        text = [text]

    my_url_translate = TRANSLATE_URL + language

    for query in text:
        q = "&q="
        text_encoded = urllib.quote(query)
        my_url_translate += q + text_encoded

    url = my_url_translate
    http = httplib2.Http()
    response, body = http.request(url, "GET")
    parsed_body = json.loads(body)

    print(parsed_body)

    for idx, val in enumerate(text):
        translatedText = parsed_body['data']['translations'][idx]['translatedText']
        translatedText1.append(translatedText.encode('utf-8'))

    return translatedText1


def twilio(to, message, reciever, language):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to=to,
        from_=reciever,
        body=googleTranslate([message[2]], language))
    print(message[2])


twilio("+14083688346", text, "+18173857835", "es")
