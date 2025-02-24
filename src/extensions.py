from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

#tiro esse mashmallow?

db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()
