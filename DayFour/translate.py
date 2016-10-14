#!/usr/bin/env python3
import httplib2
import json


def translatedText(text_to_translate, language_code):
    GOOGLE_API_KEY = "AIzaSyBvaNeZczwFLD8vOa6UNX4KZajB4h_0bSw"
    TRANSLATE_URL = "https://www.googleapis.com/language/translate/v2"

    TRANSLATE_URL += '?'
    TRANSLATE_URL += 'q=' + text_to_translate
    TRANSLATE_URL += 'target=' + language_code
    TRANSLATE_URL += 'key=' + GOOGLE_API_KEY

    http = httplib2.Http()
    response, body = http.request(TRANSLATE_URL, "GET")

    parsed_body = json.loads(body)

    translatedText = parsed_body['data']['translations'][0]['translatedText']
    return translatedText
