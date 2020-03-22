from flask import Flask
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}:{}@localhost:5432/students".format("postgres", "admin123")

from api.students import students_blueprint
app.register_blueprint(students_blueprint)