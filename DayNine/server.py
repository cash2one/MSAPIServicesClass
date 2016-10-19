from flask import Flask, request
import json

app = Flask(__name__)
petShop = []


@app.route("/hello")
def hello():
    return "Hello World!"


'''
:seven: Add a new handler that receives PUT requests to the route
`/pets/<name>` and checks if a pet with that `name` exists. If not, respond
with a HTTP 404 error and a helpful JSON error message. If so, validate the
JSON data sent in the request body and update the pet with that `name` with the
new fields. If validation fails, respond with HTTP 400 error.
'''


@app.route("/pets/<name>", methods=['PUT'])
def update_pet(name):
    result = request.form
    if(name and result['age'] and result['species']):
        for (index, pet) in enumerate(petShop):
            if(pet['name'] == name):
                newPet = {
                    "age": result['age'],
                    "name": name,
                    "species": result["species"]
                }
                petShop.pop(index)
                petShop.append(newPet)
                return json.dumps(newPet, sort_keys=True)
        content = '{err: "Pet with that name wasn\'t found"}'
        return content, 404
    else:
        content = '{err: "Missing params"}'
        return content, 400


@app.route("/pets", methods=['POST'])
def store_pets():
    result = request.form
    if(result['name'] and result['age'] and result['species']):
        if([x for x in petShop if x['name'] == result['name']] == []):
            petShop.append(result)
            return json.dumps(result, sort_keys=True)
        else:
            content = '{err: "Pet with that name already exists"}'
            return content, 409
    else:
        content = '{err: "Missing params"}'
        return content, 400


@app.route("/pets", methods=['GET'])
def get_pets():
    return json.dumps(petShop, ensure_ascii=False, sort_keys=True)


@app.route("/pets/<name>", methods=['GET'])
def get_pet_with_name(name):
    return json.dumps(
        [x for x in petShop if x['name'] == name], sort_keys=True)


@app.route("/pets/<name>", methods=['DELETE'])
def delete_pet_with_name(name):
    for (index, pet) in enumerate(petShop):
        if(pet['name'] == name):
            tempItem = petShop[index]
            petShop.pop(index)
            return json.dumps(tempItem, sort_keys=True)
    content = '{err: "Pet with that name wasn\'t found"}'
    return content, 404


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
