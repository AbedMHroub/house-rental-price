import flask
from flask import Flask, request , jsonify
import pandas as pd
from datetime import datetime as dt
from joblib import dump, load

with open('priceprediction.joblib', 'rb') as f:
    model = load(f)

app = Flask(__name__)


@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == "GET":
        predict = model.predict([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
        return jsonify({"response":"get abed " + predict})
    elif request.method == "POST":
        req_json = request.json
        city = req_json['city']
        '''
        status = req_json['status']
        rooms  = req_json['rooms']
        bathrooms  = req_json['bathrooms']
        balconies   = req_json['balconies']
        houseSpace   = req_json['houseSpace']
        elevator  = req_json['elevator']
        carParking  = req_json['carParking']
        heating  = req_json['heating']
        f1 = bathrooms/rooms
        f2 = (balconies + bathrooms) / rooms
        ba = 1
        bb = 1
        msh = 1
        ce = 1
        '''
        #predict = model.predict([[city,status,rooms,bathrooms,balconies,houseSpace,elevator,carParking,heating,f1,f2,ba,bb,msh,ce]])[0]
        return jsonify({"response": "hi "+ city+"status+rooms+bathrooms+balconies+houseSpace+elevator+carParking+heating ++f1+f2+ba+bb+msh+ce" })
        #return jsonify({"response": "hi "+ city+status+rooms+bathrooms+balconies+houseSpace+elevator+carParking+heating +"+f1+f2+ba+bb+msh+ce" })
if __name__ == '__main__':
    app.run(debug=True,port=9090)

'''
    city = ""
    status = int(request.args['status'])
    "rooms" : " ",
    "bathrooms" : "",
    "balconies" : " ",
    "houseSpace" : " ",
    "elevator" : " ",
    "carParking" : " "
    "heating" : " ",

    "status" : "1",
	"rooms" : "1",
    "bathrooms" : "1",
    "balconies" : "1",
    "houseSpace" : "1",
    "elevator" : "1",
    "carParking" : "1",
    "heating" : "1"
    try:
        return city
    except KeyError:
        return f'Invalid input ()'
        
        '''