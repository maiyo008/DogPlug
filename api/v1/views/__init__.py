""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.county import *
from api.v1.views.dog import *
from api.v1.views.groomer import *
from api.v1.views.owner import *