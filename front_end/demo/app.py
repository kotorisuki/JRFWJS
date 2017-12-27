import os
#import sqlite3
import base64
import json
from originSourceCode import LargeDataCalc, integration, drawPictures
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, send_from_directory
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_object(__name__) # load config from this file , app.py
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, "upload")
app.config['STATIC_FOLDER'] = os.path.join(app.root_path, "static")

# Load default config and override config from an environment variable
#app.config.update(dict( \
#	DATABASE=os.path.join(app.root_path, 'app.db'), \
#))

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
	return render_template("page%d.html" % page_id, results = None, error = None)

@app.route("/query/<int:page_id>", methods=['POST'])
def query(page_id):
	if page_id == 1:
		results = dict()
		m = float(request.form['fv'])
		c = float(request.form['cr']) / 100
		timeStart = request.form['id']
		period = int(request.form['yn'])
		timeCurrent = request.form['pd']
		frequency = int(request.form['pf'])
		pv, yy, dd, cc = integration.integration(c, m, timeStart, period, timeCurrent, frequency)
		results['Pv'] = pv
		results['Yield'] = yy
		results['Duration'] = dd
		results['Convexity'] = cc
		return render_template("page1.html", results=results, error=None)
	elif page_id == 2:
		file_dir = app.config['UPLOAD_FOLDER']
		if not os.path.exists(file_dir):
			os.makedirs(file_dir)
		# check if the post request has the file part
		if 'file' not in request.files:
			return render_template("page2.html", results=None, error="No File Part!")
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
			return render_template("page2.html", results=None, error="No Selected File!")
		if file:
			filename = base64.b64encode(file.filename) + ".json"
			filename = secure_filename(filename)
			fakeyPng = filename[:-5] + "yield" + ".png"
			fakedPng = filename[:-5] + "duration" + ".png"
			fakecPng = filename[:-5] + "convexity" + ".png"
			fakeresultfilename = filename[:-5] + "result" + ".json"
			filename = os.path.join(file_dir, filename)
			yPng = os.path.join(app.config['STATIC_FOLDER'], fakeyPng)
			dPng = os.path.join(app.config['STATIC_FOLDER'], fakedPng)
			cPng = os.path.join(app.config['STATIC_FOLDER'], fakecPng)
			resultfilename = filename[:-5] + "result" + ".json"
			if os.path.isfile(filename):
				os.remove(filename)
			file.save(os.path.join(filename))
			LargeDataCalc.data_input(filename, resultfilename)
			with open(resultfilename) as json_file:
				results = json.load(json_file)
			drawPictures.drawPicture(results, yPng, dPng, cPng)
			cnt = len(results)
			for i in xrange(cnt):
				results[i]['Id'] = i
			return render_template("page2.html", results=results, error=None, resultfilename = fakeresultfilename, yPng = fakeyPng, dPng = fakedPng, cPng = fakecPng)
		return render_template("page2.html", results=None, error="Unknown Error!")
	else:
		abort(404)

@app.route('/uploads/<path:filename>')
def download(filename):
	filename = secure_filename(filename)
	if request.method=="GET":
		print filename
		if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
			return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
	abort(404)

if __name__ == "__main__":
	app.run()
