from flask import Flask,json,jsonify,Blueprint,request
from app.views.incidents import incident
import datetime
import re

user_print = Blueprint('user_print', __name__)
users = []

@user_print.route('/api/v1/users', methods=['GET'])
def getall_users():

    ####returns a list of all users
    if len(users) ==0:
        return jsonify({"message": "No users yet", "count": len(users)}), 200

    return jsonify({"users": users, "count": len(users)}), 200


@user_print.route('/api/v1/users', methods=['POST'])
def create_user():
    #### creates a new user
    if not request.content_type == 'application/json':
        return jsonify({"failed": "content-type must be application/json"}), 401
    request_data = request.get_json()
    if not is_valid_user_request(request_data):
        return jsonify({"success": False, "message": "Bad Request"}), 400

    if not is_valid(request_data['email']):
        return jsonify({"success": False, "message": "Email is badly formatted"}), 401
    newuser = {
        "user_id": len(users) + 1,
        "firstname":request_data['firstname'],
        "lastname":request_data['lastname'],
        "othernames":request_data['othernames'],
        "email":request_data['email'],
        "phone_number":request_data['phone_number'],
        "username":request_data['username'],
        "registered":datetime.datetime.utcnow(),
        "is_admin":request_data['is_admin']

    }
    if len(users) == 0:
        users.append(newuser)
        return jsonify({"success": True, "user_id": newuser.get('user_id') }), 201

    for user in users:
        if user['email'] == request_data['email']:
            return jsonify({"success": False, "message": "Email is already taken"}), 401
        if user['username'] == request_data['username']:
            return jsonify({"success": False, "message": "Username is already taken"}), 401
    users.append(newuser)
    return jsonify({"success": True, "user_id": newuser.get('user_id')}), 201


def is_valid_user_request(newuser):
    ### checking valid feilds

    if "firstname" in newuser and "lastname" in newuser and "phone_number" in newuser and "email" in newuser and "password" in newuser:
        return True
    else:
        return False


def is_valid(email):
    ###validating an email

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True