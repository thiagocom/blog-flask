# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateTutorial(FlaskForm):
		
	"Form to create a tutorial"

	title = StringField("title", validators=[ DataRequired() ])
	file = FileField(validators=[ FileRequired() ])
	submit = SubmitField("Send Tutorial")
