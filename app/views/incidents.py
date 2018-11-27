from flask import Flask,json,jsonify,Blueprint,request
import datetime

incident=Blueprint('incident',__name__)
crimes=[]
@incident.route('/',methods=['GET'])
def index():
    return jsonify({'message':"welcome"}),200

@incident.route('/red-flags',methods=['GET'])
def getred_flags():
        return jsonify({'data':crimes}),200


@incident.route('/red-flags',methods=['POST'])
def postred_flags():
    data=request.get_json()
      #TODO VALIDATE
    crime={
          "id":len(crimes)+1,
          "created_on":datetime.datetime.utcnow(),
          "comment":data['comment']

    }
    crimes.append(crime)
    return jsonify({"success":True,"crime":crime.get('id')}),201
    