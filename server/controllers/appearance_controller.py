from flask import request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.config import db

@jwt_required()
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify({'message': 'Appearance created', 'id': appearance.id}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400