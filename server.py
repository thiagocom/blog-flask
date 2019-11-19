# -*- coding: utf-8- *-

from app import create_app
from config import Config, DevelopmentConfig

def select_config_class(env):

	config_class = Config
	if env == "development":
		config_class = DevelopmentConfig
	return config_class

config_class = select_config_class(os.getenv("FLASK_ENV"))

app = create_app(config_class)
