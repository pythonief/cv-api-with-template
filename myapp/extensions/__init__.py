"""
Extensions for the main application, like database or form extension utilities
"""

"""
Import and initialize extensions:
Example:

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

"""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class SQLBaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        entities = cls.query.all() or None
        return entities

    @classmethod
    def get_entity_by_id(cls, pk):
        entity = cls.query.filter_by(id=pk).first()
        print(entity)
        return entity
