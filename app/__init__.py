# -*- coding: utf-8 -*-

from flask import Flask
from flask_migrate import Migrate
from database import db

def create_app(config_class):

	app = Flask("app")
	app.config.from_object(config_class)

	db.init_app(app)
	Migrate(app, db)

	from blueprints import blog

	app.register_blueprint(blog.bp)

	return app
