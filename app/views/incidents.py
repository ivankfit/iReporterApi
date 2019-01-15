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
@incident.route('/api/v1/red-flags/<int:id>',methods=['GET'])
def get_specific_red_flag(id):

      if not item_exists(id, incidents):
            return jsonify({'msg':'item not found'}), 404
      #find the item by id
      for incident in incidents:
            if incident['id'] == id:
                  return jsonify({'data' :incident}),200
      
@incident.route('/api/v1/red-flags',methods=['POST'])
def postred_flags():
    data=request.get_json()
    if not request.content_type is 'application/json':
        return jsonify({"failed": "content-type must be application/json"}), 401
    
           
    crime={
          "id":len(crimes)+1,
          "created_on":datetime.datetime.utcnow(),
          "created_by":1,
          "type":data['type'],
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
      if not item_exists(id,crimes):
            return jsonify({'msg':'item not found'}),404
      #CREATE A NEW LIST OBJECT
      data=request.get_json()
            #TODO VALIDATE
      crime={
            "id":id,
            "last_updated_on":datetime.datetime.utcnow(),
            "created_by":1,
            "crime_nature":data['crime_nature'],
            "location":data['location'],
            "status":data['status'],
            "images":data['image'],
            "video":data['image'],
            "comment":data['comment']


      }
      for i in crimes:
          if i['id']==id:
                pass
      return jsonify({"msg":"updated"}),200

@incident.route('/api/v1/red-flags/<int:id>',methods=['DELETE'])
def delete_red_flags(id):
    #find the item by id
    if not item_exists(id,crimes):
       return jsonify({'msg':'item not found'}),404

    for crime in crimes:
        if crime['id']==id:
           crimes.remove(crime)
    return jsonify({'Message': "item deleted"}),200
    

def item_exists(item_id,itemlist):
      for item in itemlist:
            if item['id']==item_id:
                  return True
      return False