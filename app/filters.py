# -*- coding: utf-8 -*-

def register_filters(app):

	@app.template_filter()
	def concat(arg1, arg2):
		"Concat strings"
		return str(arg1) + str(arg2)
