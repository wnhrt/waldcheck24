from flask import Blueprint, render_template, request, current_app, url_for
from werkzeug.utils import redirect
from flask import flash

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
	wald = Wald.query.get(wald_id)
	return render_template('wald/details.html', wald=wald)

@bp_wald.route('/create', methods=["POST", "GET"])
def create():
	if request.method == "POST":
			flaeche = float(request.form.get('flaeche'))
			forstung = bool(request.form.get('forstung'))
			lokation = str(request.form.get('lokation'))
			name = request.form.get('name')
			#neuer_wald_eintrag = Wald(flaeche=flaeche, forstung=forstung, lokation=lokation, name=name)
			wald = Wald()
			wald.flaeche = flaeche
			wald.lokation = lokation
			wald.forstung = forstung if forstung else False
			wald.name = name

			if not flaeche:
				flaeche = 99
				flash('bitte flache eingeben', 'error')

			if not forstung:
				forstung = True
				flash('bitte forstung eingeben', 'error')

			if not lokation:
				lokation = 'xyz'
				flash('bitte lokation eingeben', 'error')

			if not name:
				name = 'failed'
				flash('bitte name eingeben', 'error')

			print('\n'*10)
			print(wald.forstung)
			print(wald.flaeche)
			print(wald.lokation)
			print(wald.name)
			print('\n'*10)
			db.session.add(wald)
			db.session.commit()
			return redirect(url_for('wald.overview'))


	return render_template('wald/create.html')
