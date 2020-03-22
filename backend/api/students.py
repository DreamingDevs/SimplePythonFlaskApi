from flask import request, Blueprint, jsonify
from datetime import datetime
from models import student
from util.decorators import token_required

students_blueprint = Blueprint('students', __name__)

@students_blueprint.route('/', methods=['GET'])
@token_required
def home(*args, **kwargs):
    now = datetime.now()
    return "Hello, Flask!"

@students_blueprint.route('/student', methods=['POST', 'GET'])
def handle_student():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            student.create_student(name = data['name'])
            return {"message": f"Student {data['name']} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        students = student.fetch_all()
        results = [
            {
                "name": student.name
            } for student in students]

        return {"count": len(results), "students": results}