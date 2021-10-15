from waldcheck24.app import db
from faker import Faker
from .models import *


from pathlib import Path

class DatabaseFiller:
	def __init__(self, db):
		self.faker = Faker()
		self.init_wald(db)

	def init_wald(self, db):
		for x in range(5):
			wald = Wald()
			wald.name = self.faker.name()
			wald.flaeche = 50
			wald.lokation = 'abc'
			wald.forstung = True
			db.session.add(wald)
		db.session.commit()



#db.create_all()