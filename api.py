# import libraries
from flask import Flask, request

app = Flask(__name__)


#http://127.0.0.1:5000/
@app.route('/')
def welcome():
    return"Welcome To Flask Api"

#http://127.0.0.1:5000/
@app.route('/predict')
def welcome():
    input = request.args.get('input')
    return"The input fed is" + str(input)


if __name__ == "__main__":
    app.run()
