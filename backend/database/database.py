from api import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy(app)
db.init_app(app)
db.Model.metadata.reflect(db.engine)
migrate = Migrate(app, db)