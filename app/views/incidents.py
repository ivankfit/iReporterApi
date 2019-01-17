import datetime
from flask import jsonify, Blueprint, request
from werkzeug import secure_filename

incident = Blueprint('incident', __name__)
incidents = []


@incident.route('/', methods=['GET'])
def index():
    """creates a welcome page"""
    return jsonify({'message': "welcome"}), 200


@incident.route('/api/v1/red-flags', methods=['POST'])
def postred_flags():
    """ creates ared flag"""
    data = request.get_json()
    if request.content_type != 'application/json':
        return jsonify(
            {"failed": "content-type must be application/json"}), 401

    if 'comment' not in data:
        return jsonify(
            {'msg': 'comment missing! please supply in the comment'}), 400

    if len(data['comment']) < 5:
        return jsonify(
            {'message': 'comment too short! please supply long text'}), 400

    incident = {
        "id": len(incidents) + 1,
        "created_on": datetime.datetime.utcnow(),
        "created_by": 1,
        "type": data['type'],
        "location": data['location'],
        "status": 'draft',
        "comment": data['comment']
    }
    incidents.append(incident)
    return jsonify({"success": True, "incident": incident.get('id')}), 201


@incident.route('/api/v1/red-flags', methods=['GET'])
def getred_flags():
    """gets all red flags"""
    return jsonify({'data': incidents}), 200


@incident.route('/api/v1/red-flags/<int:specific_id>', methods=['GET'])
def get_specific_red_flag(specific_id):
    """ gets a specific redflag"""
    if not item_exists(specific_id, incidents):
        return jsonify({'msg': 'item not found'}), 404

    for incident in incidents:
        if incident['id'] == specific_id:
            return jsonify({'data': incident}), 200


@incident.route('/api/v1/red-flags/<int:update_id>', methods=['PUT'])
def update_specific_red_flag(update_id):
    """ updates a specific redflag"""
    if not item_exists(update_id, incidents):
        return jsonify({'msg': 'item not found'}), 404
    # CREATE A NEW LIST OBJECT
    data = request.get_json()
    for i in incidents:
        if i['id'] == update_id:
            incident_update = {
                "id": update_id,
                "last_updated_on": datetime.datetime.utcnow(),
                "created_by": 1,
                "type": data['type'],
                "location": data['location'],
                "status": "draft",
                "comment": data['comment']
            }
            i.update(incident_update)

    return jsonify({"msg": "updated"}), 200


@incident.route('/api/v1/red-flags/<int:delete_id>', methods=['DELETE'])
def delete_red_flags(delete_id):
    """deletes a redflag by id"""
    if not item_exists(delete_id, incidents):
        return jsonify({'msg': 'item not found'}), 404

    for incident in incidents:
        if incident['id'] == delete_id:
            incidents.remove(incident)
            return jsonify({'status': 200, 'Message': "item deleted"})


@incident.route('/api/v1/red-flags/<int:loc_id>/location', methods=['PATCH'])
def edit_location_of_specific_redflag(loc_id):
    """edits the location of a red flag"""
    data = request.get_json()
    if not item_exists(loc_id, incidents):
        return jsonify({'msg': 'item not found'}), 404

    for i in incidents:
        if i['id'] == loc_id:
            i['location'] = data['location']
            return jsonify({'msg': 'location updated'}), 200


@incident.route('/api/v1/red-flags/<int:com_id>/comment', methods=['PATCH'])
def edit_comment_of_specific_redflag(com_id):
    """edits comment of s red flag by id"""
    data = request.get_json()
    if not item_exists(com_id, incidents):
        return jsonify({'msg': 'item not found'}), 404
    for i in incidents:
        if i['id'] == com_id:
            i['comment'] = data['comment']

            return jsonify({'msg': 'comment updated'}), 200


def item_exists(item_id, itemlist):
    """checks if an item exists in the itemlist"""
    for item in itemlist:
        if item['id'] == item_id:
            return True
    return False
