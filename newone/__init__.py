from datetime import  timedelta

from flask import Flask, make_response
from flask_restful import Api, Resource
from pymongo import MongoClient
from flask_jwt_extended import jwt_required, JWTManager, create_access_token

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "zankano-tachi"
jwt = JWTManager(app)

JWT_ACCESS_TOKEN_TIMEDELTA= timedelta(minutes=15)
api = Api(app)
client = MongoClient("mongodb://localhost:27017/Employees")



class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y
    def div(self, x, y):
        return x / y

    def mul(self, x, y):
        return x * y
