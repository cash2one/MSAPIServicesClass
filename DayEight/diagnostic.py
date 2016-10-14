import httplib2
import json
http = httplib2.Http()
body = '''{
    "firstName": "Grace",
    "lastName": "Hopper",
    "age": 107,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": 10021
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "212-555-1234"
        },
        {
            "type": "mobile",
            "number": "646-555-4567"
        }
    ]
}'''
content = json.loads(body)
print(content['address']['postalCode'])
'''
one: What is the `type` of each of the variables `body` and `content` in the
following code snippet?
```http = httplib2.Http()
# httplib2.Http
response, body = http.request(url, "GET")
# Response, Strig
content = json.loads(body)
# Object

:two: How would you access Grace Hopper’s postal code? (Write your response as
a Python code snippet.)
# content['address']['postalCode']

:three: How would you access her mobile phone number? (Write your response as a
Python code snippet.)
# content['phoneNumbers'][1]['number']
'''
