from database.database import db

class student(db.Model):
    __tablename__ = "students"
    __table_args__ = {"extend_existing":True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<student %r>' % self.name


def create_student(name):
    student_object = student(name)
    db.session.add(student_object)
    db.session.commit()

def fetch_all():
    return student.query.all()
