from flask import Flask

def create_app():
	app = Flask('waldcheck24')

	from .frontend import bp_frontend
	app.register_blueprint(bp_frontend)

	return app