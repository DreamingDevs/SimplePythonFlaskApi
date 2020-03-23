from database.database import db

class teacher(db.Model):
    __table__ = db.Model.metadata.tables['teachers']


def fetch_all():
    return teacher.query.all()