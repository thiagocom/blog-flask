# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

bp = Blueprint("blog", "blog")

@bp.route("/")
def index():
	return render_template("blog/index.html")


@bp.route("/")
def create_post():
	return render_template("blog/create_post.html")
