from flask import render_template as HTML, make_response as Response
from flask_restful import Resource
from flask_jwt import jwt_required


class Admin:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


class AdminLogin(Resource):
    # [GET] Login page for the admin
    @jwt_required()
    def get(self):
        headers = {"Content-Type": "text/html"}
        return Response(HTML("index.html"), 200, headers)


class AdminManage(Resource):
    # [GET] Manage admin page
    @jwt_required()
    def get(self):
        headers = {"Content-Type": "text/html"}
        return Response(HTML("admin_management.html"), 200, headers)
