from flask import request, Blueprint, jsonify
from models import teacher

teachers_blueprint = Blueprint('teachers', __name__)

@teachers_blueprint.route('/teachers', methods=['GET'])
def get_teachers():
    teachers = teacher.fetch_all()
    results = [
        {
            "name": teacher.name
            } for teacher in teachers]
    return jsonify(results)