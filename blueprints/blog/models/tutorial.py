# -*- coding: utf-8 -*-

from database import db

class Tutorial(db.Model):

	__tablename__ = "tutorials"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, unique=True)
	slug = db.Column(db.String)
	filename = db.Column(db.String)

	def __repr__(self):
		return "<Tutorial: {}>".format(self.title)
