from waldcheck24.app import db


class Wald(db.Model):
	wald_id = db.Column(db.Integer, primary_key=True)
	flaeche = db.Column(db.Float, nullable=False)
	forstung = db.Column(db.Boolean, nullable=False)
	lokation = db.Column(db.String(100), nullable=False)
	name = db.Column(db.String(100), nullable=False)
	baumbestand = db.relationship('Baumbestand')
	ertragsklasse = db.relationship('Ertragsklasse')
	bewertung = db.relationship('Bewertung')

class Baumbestand(db.Model):
	baumbestand_id = db.Column(db.Integer, primary_key=True)
	wald_id = db.Column(db.Integer, db.ForeignKey('wald.wald_id'), nullable=False)
	baumart_id = db.Column(db.Integer, db.ForeignKey('baumart.baumart_id'), nullable=False)
	alter = db.Column(db.Integer, nullable=False)
	flaeche_baumbestand = db.Column(db.Float, nullable=False)
	bewertung = db.relationship('Bewertung')
	baumart = db.relationship('Baumart')


class Baumart(db.Model):
	baumart_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)

class Ertragsklasse(db.Model):
	ertragsklasse_id = db.Column(db.Integer, primary_key=True)
	wald_id = db.Column(db.Integer, db.ForeignKey('wald.wald_id'), nullable=False)
	alter = db.Column(db.Integer, nullable=False)
	preis = db.Column(db.Float, nullable=False)


class Bewertung(db.Model):
	bewertung_id = db.Column(db.Integer, primary_key=True)
	wald_id = db.Column(db.Integer, db.ForeignKey('wald.wald_id'), nullable=False)
	baumbestand_id = db.Column(db.Integer, db.ForeignKey('baumbestand.baumbestand_id'), nullable=False)
	datum = db.Column(db.Date, nullable=False)