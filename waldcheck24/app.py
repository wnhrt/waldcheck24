from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path

db = SQLAlchemy()

def create_app():
	app = Flask('waldcheck24')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	app.config['SECRET_KEY'] = 'super secret key'

	db.init_app(app)

	from .frontend import bp_frontend
	app.register_blueprint(bp_frontend)

	if not Path(app.root_path + '/database.db').exists():
		from .database_init import DatabaseFiller
		with app.app_context():
			db.create_all()
			DatabaseFiller(db)

	from .wald import bp_wald
	app.register_blueprint(bp_wald, url_prefix='/wald')

	return app
