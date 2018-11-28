from flask import Flask,json,jsonify,Blueprint,request
import datetime

incident=Blueprint('incident',__name__)
crimes=[]
@incident.route('/',methods=['GET'])
def index():
    return jsonify({'message':"welcome"}),200

@incident.route('/api/v1/red-flags',methods=['GET'])
def getred_flags():
        return jsonify({'data':crimes}),200

  #getting a specific red flag
@incident.route('/api/v1/red-flags<int:id>',methods=['GET'])
def get_specific_red_flag(id):
      #find the item by id
      for crime in crimes:
            if crime['id'] == id:
                  return jsonify({'message': 'crime found'})
      return jsonify({'data' :crimes}),200


@incident.route('/api/v1/red-flags',methods=['POST'])
def postred_flags():
    data=request.get_json()
      #TODO VALIDATE
    crime={
          "id":len(crimes)+1,
          "created_on":datetime.datetime.utcnow(),
          "created_by":1,
          "crime_nature":data['crime_nature'],
          "location":data['location'],
          "status":data['status'],
          "images":data['image'],
          "video":data['image'],
          "comment":data['comment']


    }
    crimes.append(crime)
    return jsonify({"success":True,"crime":crime.get('id')}),201

#####Editing aspecific flag
@incident.route('/api/v1/red-flags/<int:id>',methods=['PUT'])
def update_specific_red_flag(id):
      if not incident:
            return jsonify({'message': 'No crime found!'})
      crimes.complete = True
      return jsonify({'message': 'Incident item has been completed!'})


@incident.route('/api/v1/red-flags/<int:id>',methods=['DELETE'])
def delete_red_flags(id):
    #find the item by id
    for crime in crimes:
        if crime['id']==id:
           crimes.remove(crime)
    return jsonify({'Message': "Crime deleted"})
    