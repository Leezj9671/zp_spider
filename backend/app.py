from flask import Blueprint
from flask_restful import Api
from resources.EmployInfo import EmployInfoResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(EmployInfoResource, '/jobs')
api.add_resource(EmployInfoResource, '/jobs/<string:keyword>', endpoint="keyword")