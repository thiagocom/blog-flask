# -*- coding: utf-8 -*-

from database import db

class Post(db.Model):

	__tablename__ = "posts"

	id = db.Column(db.String, primary_key=True)
	title = db.Column(db.String, unique=True)
	slug = db.Column(db.String)

	def __repr__(self):
		return "<Post: {}>".format(self.title)
