# -*- coding: utf-8 -*-

import os.path

class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PER_PAGE = 1
    SECRET_KEY = "S3cr3t-k3y"
    ALLOWED_EXTENSIONS = ["md"]
    UPLOADS_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__name__), "app", "static", "pages"))


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.abspath(os.path.join(os.path.dirname(__name__), "dev.db"))


class ProductionConfig(Config):

	SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
            os.path.abspath(os.path.join(os.path.dirname(__name__), "app.db"))

