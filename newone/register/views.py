from datetime import timedelta

from newone.register.controller import find_user, reg_user, rm_user ,update_user_pwd
from newone import api, Resource, make_response, app, JWT_ACCESS_TOKEN_TIMEDELTA
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

regblue = Blueprint('registerblue', __name__)


class Register(Resource):
    def post(self):
        try:
            data = request.get_json()

            username = data.get('username')
            password = data.get('password')
            if not username and not password:
                return make_response(jsonify({"message": "User not found"}), 200)
            existing_user = find_user(username)
            if existing_user:
                return make_response(jsonify({"message": 'User already exists'}), 200)
            new_user = {"username": username, "password": password}
            result = reg_user(new_user)
            if result:
                return make_response(jsonify(
                    {"Message": "User registered successfully", "userName": username,
                     "userid": str(result.inserted_id)}))
        except Exception as e:
            print(e)


class Login(Resource):
    def post(self):

        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        userinfo = find_user(username)
        usernamedb = userinfo.get("username")
        passworddb = userinfo.get("password")

        if username == usernamedb and password == passworddb:
            access_token = create_access_token(identity=username, expires_delta=JWT_ACCESS_TOKEN_TIMEDELTA)
            return make_response(jsonify({"Message": "User logged in successfully", "Access_Token": access_token}))
        else:
            return make_response(jsonify({"Message": "Invalid Credentials"}))


class removeUser(Resource):

    @jwt_required()
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        userInfo = find_user(username)
        if userInfo:
            usernamedb = userInfo.get("username")
            passwordDB = userInfo.get("password")
        else:
            return make_response(jsonify({"message": 'User not found'}))
        print(usernamedb, passwordDB)

        if usernamedb is None:
            return make_response(jsonify({"message": 'User not found'}))
        delete_user = {"username": username, "password": password}
        print(username)
        result = rm_user(username)
        if result:
            return make_response(jsonify({"Message": "user deleted"}))
        else:
            return make_response({"message": "User is already delete or not found"})

class UpdateUserPassword(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        username = get_jwt_identity()
        current_password = data["current_password"]
        new_password = data["new_password"]

        dbdata = find_user(username)
        userdb = dbdata["username"]
        passworddb = dbdata["password"]

        if current_password == passworddb:
            update_user_pwd(username, new_password)

            return make_response(jsonify({"message": "Info updated successfully"}))


api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(removeUser, '/removeuser')
api.add_resource(UpdateUserPassword, '/update')
