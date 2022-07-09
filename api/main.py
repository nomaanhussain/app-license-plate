from . import util
from .models import *
from flask import Blueprint, request, jsonify

from api import app



@app.route("/", methods=['GET'])
@util.exception_handler
def home():
    return "ok", 200


@app.route("/plate", methods=['POST'])
@util.exception_handler
def add_plate():
    
    params = request.json

    plate = params['plate'] if 'plate' in params else None 

    if not plate:
        return jsonify({
                'status': 'error',
                'error': "Missing parameter: plate"
            }), 400

    try:
        LicensePlate.add(plate)
    except (AssertionError) as err:
        return jsonify({
                'status': 'error',
                'error': str(err)
            }), 422

    return jsonify({"response": "added"}), 200


@app.route("/plate", methods=['GET'])
@util.exception_handler
def get_plates():
    
    
    licence_plates = LicensePlate.query.all()

    response = []
    for row in licence_plates:
        response.append({
            "plate": row.plate,
            "timestamp": row.timestamp
        })

    return jsonify(response), 200



@app.route("/search-plate", methods=['GET'])
@util.exception_handler
def search_plates():
    
    key = request.args.get('key', '')
    levenshtein = request.args.get('levenshtein', 0)

    licence_plates = LicensePlate.search(key, levenshtein)

    response = []
    for row in licence_plates:
        response.append({
            "plate": row.plate.replace('-', ''),
            "timestamp": row.timestamp
        })

    return jsonify(response), 200


