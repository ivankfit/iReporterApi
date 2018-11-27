from flask import Flask,Blueprint
from app.views.incidents import incident
app=Flask(__name__)
app.register_blueprint(incident)
