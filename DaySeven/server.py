from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/pets", methods=['POST'])
def storePets():
    result = request.form
    print(result["name"])
    return str(result)


@app.route("/pets", methods=['GET'])
def getPets():
    result = request.form
    print(result["name"])
    return json.dumps(result, ensure_ascii=False)


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
