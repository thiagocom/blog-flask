# -*- coding: utf-8 -*-

from flask import (
	Blueprint, render_template, request, redirect, url_for, current_app, flash
)
from werkzeug.utils import secure_filename
from slugify import slugify
import os.path
from .models import Tutorial
from .forms import CreateTutorial
from database import db
from markdown2 import markdown

bp = Blueprint("blog", "blog")

def allowed_file(filename):
	return "." in filename and \
		filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]

@bp.route("/")
@bp.route("/index")
def index():
	page = request.args.get("page", 1, type=int)
	per_page = current_app.config["PER_PAGE"]
	tutorials = Tutorial.query.paginate(page, per_page, False)
	return render_template("blog/index.html", tutorials=tutorials)

@bp.route("/create-tutorial", methods=["GET", "POST"])
def create_tutorial():
	form = CreateTutorial()
	if form.validate_on_submit():
		title = form.title.data
		if (not Tutorial.query.filter_by(title=title).first()):
			file = form.file.data
			if allowed_file(file.filename):	
				slug = slugify(title)
				extension = os.path.splitext(file.filename)[1]
				filename = secure_filename("{}{}".format(slug, ".html"))
				tutorial = Tutorial(title=title, slug=slug, filename=filename)
				pathname = os.path.join(current_app.config["UPLOADS_FOLDER"], filename)
				with open(pathname, "w") as f:
					content = markdown(file.read())
					f.write(content)
				#file.save(current_app.config["UPLOADS_FOLDER"], filename)
				db.session.add(tutorial)
				db.session.commit()
				flash("Tutorial created with successfully", category="success")
				return redirect(url_for("blog.index"))
			else:
				flash("File extension not allowed", category="warning")
		else:
			flash("Title already in use", category="warning")
	return render_template(
		"blog/create_tutorial.html", form=form, title="Create tutorial"
	)

@bp.route("/<slug>")
def see_tutorial(slug):
	tutorial = Tutorial.query.filter_by(slug=slug).first_or_404()
	return render_template("blog/see_tutorial.html", tutorial=tutorial, title=tutorial.title)
