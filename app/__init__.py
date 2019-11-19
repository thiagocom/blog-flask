# -*- coding: utf-8 -*-

from flask import Flask

def create_app(config_class):

	app = Flask("app")
	app.config.from_object(config_class)

	return app
