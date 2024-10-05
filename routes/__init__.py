from flask import Blueprint
from .user.registarion import registarion

def register_blueprints(app):
    app.register_blueprint(registarion)
