from flask import Flask, request
import json

app = Flask(__name__)
petShop = []


@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"


'''
Modify the `/pets` handler to parse the JSON data, validate that it has *all*
of these fields: `name`, `age`, `species`. If it passes validation, store the
parsed dictionary in a simple list variable (this will serve as a temporary
in-memory database so these pets will be saved for the lifetime of the web
server). If not, respond with a HTTP 400 error and a helpful error message in
JSON. Test the `/pets` route to ensure it responds correctly to *both* valid
and invalid POST requests.
'''


@app.route("/pets", methods=['POST'])
def store_pets():
    result = request.form
    if(result['name'] and result['age'] and result['species']):
        petShop.append(result)
        return json.dumps(result)
    else:
        content = '{err: "Missing params"}'
        return content, 400


@app.route("/pets", methods=['GET'])
def get_pets():
    return json.dumps(petShop, ensure_ascii=False)


@app.route("/pets/<name>", methods=['GET'])
def get_pet_with_name(name):
    return json.dumps([x for x in petShop if x['name'] == name])


@app.route("/fizzBuzz")
def fizzBuzz():
    valToReturn = ""
    num = int(request.args.get('q'))
    if(num % 3 == 0 and num % 5 == 0):
        valToReturn = "fizzBuzz"
    elif(num % 3 == 0):
        valToReturn = "fizz"
    elif(num % 5 == 0):
        valToReturn = "buzz"
    else:
        valToReturn = str(num)

    return json.dumps({"cod": 200, "val": valToReturn})

if __name__ == "__main__":
    app.run()
