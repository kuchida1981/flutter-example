import os
from flask_restx import Api
from . import resources

firebase_authorization = {
    "type": "apiKey",
    "in": "header",
    "name": "Authorization",
    "description": "Firebase Authentication で得られるIDトークンを受け取る",
}

local_authorization = {
    "type": "apiKey",
    "in": "header",
    "name": "X-Firebase-UID",
}

if os.getenv("FLASK_ENV") == "development":
    authorizations = {"local": local_authorization}
else:
    authorizations = {"firebase": firebase_authorization}

api = Api(
    title="Flutter Example API",
    description="Flutterと戯れるために用意したWeb API.",
    version="0.0.1",
    authorizations=authorizations,
)
resources.init(api)
