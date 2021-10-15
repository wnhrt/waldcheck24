from flask import Blueprint, render_template

bp_wald = Blueprint('wald', __name__, url_prefix='/wald')

from waldcheck24 import db

@bp_wald.route('/overview')
def overview():
	return render_template('wald/overview.html', waelder=waelder)

@bp_wald.route('/create')
def overview():
	return render_template('wald/create.html')

