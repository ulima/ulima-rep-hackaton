"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

from flask import Flask, jsonify,request
from flask.ext.cors import CORS, cross_origin
from pymongo import MongoClient
from bson.json_util import dumps
from bson import json_util
import json

@app.route('/listar/<coleccion>', methods=['GET'])
def listar_ubicaciones(coleccion):
	client = MongoClient('mongodb://ulima:ulima@ds011745.mlab.com:11745/db_rep')
	db = client.db_rep

	rpta = []

	if coleccion == "mantenimientos":
		rpta = list(db.mantenimientos.find())

	if coleccion == "ubicaciones":
		rpta = list(db.ubicaciones.find())

	if coleccion == "equipos":
		rpta = list(db.equipos.find())

	if coleccion == "cpmms":
		rpta = list(db.cpmms.find())

	return  json.dumps(rpta, default=json_util.default)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
