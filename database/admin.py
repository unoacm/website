from flask_sqlalchemy import SQLAlchemy
from database.sqldb import db as db
from werkzeug.security import (
	check_password_hash, generate_password_hash
)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	password = db.Column(db.String(64), unique=True, nullable=False) # String 64 for SHA-256 hashing

	def __init__(self, username, password):
		self.username = username
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)