from flask_jwt_extended.utils import create_refresh_token, create_access_token
from flask_restful import Resource, reqparse
import app.models.admin as adm
import app.helpers.utils as utils
import app.messages.response_errors as Err
import app.messages.responses_success as Succ


class FortAuth(Resource):
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
        admin = adm.AdminModel.find_by_username(data["username"])

        # Check password
        if admin and admin.password == utils.hash(data["password"]):
            # Create access token
            access_token = create_access_token(identity=admin.id, fresh=True)

            # Create refresh token
            refresh_token = create_refresh_token(admin.id)

            return Succ.SUCCESS_AUTHENTICATED(access_token, refresh_token)

        return Err.ERROR_INVALID_CREDS
