from flask import Blueprint, render_template

bp_wald = Blueprint('wald', __name__, url_prefix='/wald')

from waldcheck24.app import db
from waldcheck24.models import *

@bp_wald.route('/overview')
def overview():
	waelder = Wald.query.all()
	return render_template('wald/overview.html', waelder=waelder)

@bp_wald.route('/<int:wald_id>')
def details(wald_id):
	wald = None
	# TODO
	# wald = db.get_by_id(wald_id)
	return render_template('wald/details.html', wald=wald)

@bp_wald.route('/create')
def overview():
	return render_template('wald/create.html')
