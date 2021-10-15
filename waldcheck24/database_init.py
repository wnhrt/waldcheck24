from . import db
from faker import Faker
from .models import *


from pathlib import Path

class DatabaseFiller:
	def __init__(self):
		self.faker = Faker()

	def init_wald():
		pass



db.create_all()