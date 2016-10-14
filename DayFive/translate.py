import httplib2
import urllib
import json

GOOGLE_API_KEY = "AIzaSyBvaNeZczwFLD8vOa6UNX4KZajB4h_0bSw"
TRANSLATE_URL = "https://www.googleapis.com/language/translate/v2?q=asdfsfsadfd&target=es&key=asdfsadf"


def translatedText(text_to_translate, language_code):
    TRANSLATE_URL += '?'
    TRANSLATE_URL += 'q=' + urllib.quote_plus(text_to_translate)
    TRANSLATE_URL += '&target=' + language_code
    TRANSLATE_URL += '&key=' + GOOGLE_API_KEY

    http = httplib2.Http()
    response, body = http.request(TRANSLATE_URL, "GET")
    parsed_body = json.loads(str(body))
    print(parsed_body)

    translatedText = parsed_body['data']['translations'][0]['translatedText']
    return translatedText

print(translatedText("Hello", "es"))


def translatArrayOfText(array_of_text, target_language_code):
    http = httplib2.Http()
    translated_text_array = []

    for element in array_of_text:
        TRANSLATE_URL += '?'
        TRANSLATE_URL += 'q=' + urllib.quote_plus(element)
        TRANSLATE_URL += '&target=' + target_language_code
        TRANSLATE_URL += '&key=' + GOOGLE_API_KEY
        response, body = http.request(TRANSLATE_URL, "GET")
        parsed_body = json.loads(str(body))
        translated = parsed_body['data']['translations'][0]['translatedText']
        translated_text_array += translated

    return translated_text_array

english_str_arr = ["Hello", "How's it going", "My name is Alex"]
print(translatArrayOfText(english_str_arr(english_str_arr, "es")))
