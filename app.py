from flask_jwt_extended import JWTManager
from resources.tweets import (
    Tweets,
    TweetSearch,
    AuthorSearch,
    DateSearch,
    LocationSearch,
    SourceSearch,
)
from resources.admin import AdminLogin, AdminManage
from messages import response_errors as Err
from setup.settings import TwitterSettings
from models.admin import AdminModel
from helpers.utils import hash
from setup.app_config import create_app

app, api, jwt = create_app()

# Creates default admins and insert in db
for admin in TwitterSettings.get_instance().super_admins:
    admin = AdminModel(admin["email"], admin["username"], hash(admin["password"]))
    admin.insert()

# Error handlers
@app.errorhandler(404)  # Handling HTTP 404 NOT FOUND
def page_not_found(e):
    return Err.ERROR_NOT_FOUND


# API Routes
api.add_resource(Tweets, "/api/tweets")
api.add_resource(TweetSearch, "/api/tweets/tweet")
api.add_resource(SourceSearch, "/api/tweets/source")
api.add_resource(AuthorSearch, "/api/tweets/author")
api.add_resource(DateSearch, "/api/tweets/date")
api.add_resource(LocationSearch, "/api/tweets/location")

api.add_resource(AdminLogin, "/fortauth")
api.add_resource(AdminManage, "/admin/manage")

# Start the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)

