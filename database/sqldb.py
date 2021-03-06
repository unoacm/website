from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DATABASE_MODELS = [
	'Suggestion',
	'User',
	'UserAction',
	'Member',
	'Document',
	'Blog_Post',
	'Page',
	'Home_Object'
]

EDITABLE_DATABASE_MODELS = [
	'User',
	'Document',
	'Member',
	'Suggestion',
	'Blog_Post',
	'Page',
	'Home_Object'
]


def getAttributeNames(model):
	return model.__dir__()

def getTitleNames(model):
	return [attr.replace('_', ' ').strip().title() for attr in getAttributeNames(model)]

def getTitlesWithAttributes(model):
	return [(attr.replace('_', ' ').strip().title(), attr) for attr in getAttributeNames(model)]