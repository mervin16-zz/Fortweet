from flask import render_template as HTML, make_response as Response
from flask_jwt_extended.utils import create_refresh_token, create_access_token
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from app.models.admin import AdminModel
from app.helpers.utils import hash
from app.messages import response_errors as Err
from app.messages import responses_success as Succ


class AdminLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "username", type=str, required=True, help="This field cannot be blank"
    )
    parser.add_argument(
        "password", type=str, required=True, help="This field cannot be blank"
    )

    @classmethod
    def post(cls):
        # Get data from parser
        data = cls.parser.parse_args()

        # Find admin from db
        admin = AdminModel.find_by_username(data["username"])

        # Check password
        if admin and admin.password == hash(data["password"]):
            # Create access token
            access_token = create_access_token(identity=admin.id, fresh=True)

            # Create refresh token
            refresh_token = create_refresh_token(admin.id)

            return Succ.SUCCESS_AUTHENTICATED(access_token, refresh_token)

        return Err.ERROR_INVALID_CREDS


class AdminDashboard(Resource):
    # [GET] Dashboard page
    # @jwt_required
    # TODO("Enable auth here")
    def get(self):
        headers = {"Content-Type": "text/html"}
        return Response(HTML("admin/dashboard.html"), 200, headers)


class AdminAnalysis(Resource):
    # [GET] Manage analysis page
    # @jwt_required
    # TODO("Enable auth here")
    def get(self):
        headers = {"Content-Type": "text/html"}
        return Response(HTML("admin/analysis.html"), 200, headers)


class AdminManage(Resource):
    # [GET] Manage admins page
    # @jwt_required
    # TODO("Enable auth here")
    def get(self):
        headers = {"Content-Type": "text/html"}
        return Response(
            HTML("admin/admins.html", admins=AdminModel.get_all()), 200, headers
        )

    def post(self,):
        headers = {"Content-Type": "text/html"}
        return Response(
            HTML("admin/admins.html", admins=AdminModel.get_all()), 200, headers
        )


class AdminRemove(Resource):
    def post(self, id):
        print(f"Delete {id}")
        headers = {"Content-Type": "text/html"}
        return Response(
            HTML("admin/admins.html", admin_remove=True, admins=AdminModel.get_all()),
            200,
            headers,
        )


class AdminSettings(Resource):
    # [GET] Manage admin settings page
    # @jwt_required
    # TODO("Enable auth here")
    def get(self):
        headers = {"Content-Type": "text/html"}
        return Response(HTML("admin/settings.html"), 200, headers)
