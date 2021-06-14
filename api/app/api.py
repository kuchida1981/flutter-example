import os
from flask_restx import Api
from . import resources


api = Api()
resources.init(api)
