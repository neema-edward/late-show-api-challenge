from flask import jsonify
from server.models.guest import Guest
from server.config import db

def get_guests():
    guests = Guest.query.all()
    return jsonify([{'id': g.id, 'name': g.name, 'occupation': g.occupation} for g in guests]), 200