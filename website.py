from flask import (
	Flask, render_template, session
)
from flask_sqlalchemy import SQLAlchemy

from database.sqldb import db as db
import main.main as main
import blog.blog as blog
import admin.admin as admin
import database.models.admin as admin_models
import database.models.member as member_models
import database.models.suggestion as suggestion_models

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/test.db'
app.config['SECRET_KEY'] = "Gotta make sure this key is super dang long, yeehaw!"

db.init_app(app)
db.create_all()

app.register_blueprint(main.blueprint)
app.register_blueprint(blog.blueprint)
app.register_blueprint(admin.blueprint)

app.register_blueprint(admin_models.blueprint)
app.register_blueprint(member_models.blueprint)
app.register_blueprint(suggestion_models.blueprint)

if __name__ == "__main__":
	app.run()