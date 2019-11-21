# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_migrate import Migrate
from database import db

def create_app(config_class):

	app = Flask("app")
	app.config.from_object(config_class)

	db.init_app(app)
	Migrate(app, db)

	def page_not_found(error):
		return render_template("404.html"), 404

	app.register_error_handler(404, page_not_found)

	from blueprints import blog
	from .filters import register_filters
	register_filters(app)

	app.register_blueprint(blog.bp)

	return app
