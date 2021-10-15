from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
	app = Flask('waldcheck24')
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

	db.init_app(app)
	
	from .frontend import bp_frontend
	app.register_blueprint(bp_frontend)

	return app