# from django.db import models
from . import db
# Create your models here.


class MainSites(db.Model):
    id = db.Column(db.Integer, primary_keys=True)
    url = db.Column(db.String(2048), unique=True, nullabel=False)


class MalwareSites(db.Model):
    id = db.Column(db.Integer, primary_keys=True)
    url = db.Column(db.String(2048), unique=True, nullabel=False)


class PhishingSites(db.Model):
    id = db.Column(db.Integer, primary_keys=True)
    url = db.Column(db.String(2048), unique=True, nullabel=False)
