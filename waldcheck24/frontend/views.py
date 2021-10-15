from flask import Blueprint
from flask.helpers import url_for

bp_frontend = Blueprint('frontend', __name__)

@bp_frontend.route('/')
def index():
	return url_for('index.html')