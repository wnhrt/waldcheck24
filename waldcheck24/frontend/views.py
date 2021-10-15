from flask import Blueprint, render_template

bp_frontend = Blueprint('frontend', __name__)

@bp_frontend.route('/')
def index():
	return render_template('index.html')