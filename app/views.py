from django.shortcuts import render
from flask import request, jsonify
from . import app, db
from .models import MainSites
# Create your views here.


@app.route('/add_site', metods=['POST'])
def add_site():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({'error:': 'URL is required'}), 400
    new_url = MainSites(url=url)
    db.session.add(new_url)
    db.session.commit()
    return jsonify({'message': 'URL added successfully'}), 201
