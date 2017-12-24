import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
app.config.from_object(__name__) # load config from this file , app.py
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, "upload")

# Load default config and override config from an environment variable
app.config.update(dict( \
	DATABASE=os.path.join(app.root_path, 'app.db'), \
))

#def connect_db():
#	"""Connects to the specific database."""
#	rv = sqlite3.connect(app.config['DATABASE'])
#	rv.row_factory = sqlite3.Row
#	return rv
#
#def get_db():
#	"""Opens a new database connection if there is none yet for the
#	current application context.
#	"""
#	if not hasattr(g, 'sqlite_db'):
#		g.sqlite_db = connect_db()
#	return g.sqlite_db
#
#@app.teardown_appcontext
#def close_db(error):
#	"""Closes the database again at the end of the request."""
#	if hasattr(g, 'sqlite_db'):
#		g.sqlite_db.close()
#
#def init_db():
#	db = get_db()
#	with app.open_resource('schema.sql', mode='r') as f:
#		db.cursor().executescript(f.read())
#		db.commit()
#
#@app.cli.command('initdb')
#def initdb_command():
#	"""Initializes the database."""
#	init_db()
#	print('Initialized the database.')

@app.route("/")
def welcome():
	return render_template("welcome.html")

@app.route("/<int:page_id>")
def page(page_id):
	return render_template("page%d.html" % page_id)

@app.route("/query/<int:page_id>", methods=['POST'])
def query(page_id):
	return render_template("page%d.html" % page_id, results=None, error="Test")

@app.route('/upload', methods=['POST'])
def upload_file():
	file_dir=os.path.join(basedir,app.config['UPLOAD_FOLDER'])
	if not os.path.exists(file_dir):
		os.makedirs(file_dir)
	# check if the post request has the file part
	if 'file' not in request.files:
		return render_template("page%d.html" % page_id, results=None, error="No File Part!")
	file = request.files['file']
	# if user does not select file, browser also
	# submit a empty part without filename
	if file.filename == '':
		return render_template("page%d.html" % page_id, results=None, error="No Selected File!")
	if file:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return render_template("page%d.html" % page_id, results=None, error="Upload Successful!")
	return render_template("page%d.html" % page_id, results=None, error="Unknown Error!")

@app.route('/uploads/<path:filename>')
def download(filename):
	filename = secure_filename(filename)
	if request.method=="GET":
		if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
			return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
	abort(404)

if __name__ == "__main__":
	app.run()
