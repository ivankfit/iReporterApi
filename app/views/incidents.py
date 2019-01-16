from flask import Flask,json,jsonify,Blueprint,request
import datetime

incident=Blueprint('incident',__name__)
incidents=[]
@incident.route('/',methods=['GET'])
def index():
    return jsonify({'message':"welcome"}),200
# Attach an story id for creating a red flag
@incident.route('/api/v1/red-flags',methods=['POST'])
def postred_flags():
    data=request.get_json()
    if request.content_type != 'application/json':
        return jsonify({"failed": "content-type must be application/json"}), 401

    if not 'comment' in data:
          return jsonify({'msg': 'comment missing! please supply in the comment'}), 400

    if len(data['comment']) <5:
          return jsonify({'message': 'comment too short! please supply long text'}), 400  
    
           
    incident={
          "id":len(incidents)+1,
          "created_on":datetime.datetime.utcnow(),
          "created_by":1,
          "type":data['type'],
          "location":data['location'],
          "status":'draft',
          "comment":data['comment']


    }
    incidents.append(incident)
    return jsonify({"success":True,"incident":incident.get('id')}),201

@incident.route('/api/v1/red-flags',methods=['GET']) #Attach an id to get all red flags
def getred_flags():
        return jsonify({'data':incidents}),200

  #getting a specific red flag and attach an id
@incident.route('/api/v1/red-flags/<int:id>',methods=['GET'])
def get_specific_red_flag(id):

      if not item_exists(id, incidents):
            return jsonify({'msg':'item not found'}), 404
      #find the item by id
      for incident in incidents:
            if incident['id'] == id:
                  return jsonify({'data' :incident}),200   

#####Editing aspecific flag and attach an id
@incident.route('/api/v1/red-flags/<int:id>',methods=['PUT'])
def update_specific_red_flag(id):
      if not item_exists(id,incidents):
            return jsonify({'msg':'item not found'}),404
      #CREATE A NEW LIST OBJECT
      data=request.get_json()
      for i in incidents:
            if i['id'] == id:
                  incident_update={
                  "id":id,
                  "last_updated_on":datetime.datetime.utcnow(),
                  "created_by":1,
                  "type":data['type'],
                  "location":data['location'],
                  "status":"draft",
                  "comment":data['comment']
             }
                  i.update(incident_update)
                
      return jsonify({"msg":"updated"}),200

@incident.route('/api/v1/red-flags/<int:id>',methods=['DELETE'])
def delete_red_flags(id):
    #find the item by id and attach id
    if not item_exists(id,incidents):
       return jsonify({'msg':'item not found'}),404

    for incident in incidents:
        if incident['id']==id:
           incidents.remove(incident)
    return jsonify({ 'status': 200, 'Message': "item deleted"})

@incident.route('/api/v1/red-flags/<int:id>/location', methods=['PATCH'])
def edit_location_of_specific_redflag(id): #Attach the id
      data=request.get_json()
      if not item_exists(id, incidents):
            return jsonify({'msg': 'item not found'}), 404

            #TODO VALIDATE
      for i in incidents:
            if i['id'] == id:
                  i['location'] =data['location']
                  return jsonify({'msg': 'location updated'}), 200
      

@incident.route('/api/v1/red-flags/<int:id>/comment', methods=['PATCH'])
def edit_comment_of_specific_redflag(id):
      if not item_exists(id, incidents):
            return jsonify({'msge': 'item not found'}), 404
      data=request.get_json()
            #TODO VALIDATE
      for i in incidents:
            if i['id'] == id:
                  i['comment'] = data['comment']

                  return jsonify({'msg': 'comment updated'}), 200

    

def item_exists(item_id,itemlist):
      for item in itemlist:
            if item['id']==item_id:
                  return True
      return False
