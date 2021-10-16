from waldcheck24.app import db
from faker import Faker
from .models import *


from pathlib import Path

class DatabaseFiller:
	def __init__(self, db):
		self.faker = Faker()
		self.init_wald(db)

	def init_wald(self, db):
		wald = Wald()
		wald.name = 'Hölzlers Tobel'
		wald.flaeche = 6
		wald.lokation = '342'
		wald.forstung = False
		db.session.add(wald)

		wald = Wald()
		wald.name = 'Mein Wald'
		wald.flaeche = 10.7
		wald.lokation = '908'
		wald.forstung = True
		db.session.add(wald)
		db.session.commit()



#db.create_all()