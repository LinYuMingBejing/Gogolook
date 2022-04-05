from app import db
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound


EXCLUDED_FIELDS = ["creation_date", "modified_date"]


class Tasks(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    status = db.Column(db.Boolean, default = True)
    creation_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    modified_date = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now, nullable=False)


    def __init__(self, name, status):
       self.name = name
       self.status = status


    def to_dict(self):
        return {column.name: getattr(self, column.name, None) for column in self.__table__.columns if column.name not in EXCLUDED_FIELDS}


    def save(self):
        db.session.add(self)
        db.session.commit()
        return self


    def update(self, id):
        task = self.query.get(id)

        if not task:
            raise NoResultFound

        task.name = self.name
        task.status = self.status

        db.session.add(task)
        db.session.commit()
        return task


    @classmethod
    def get_all_tasks(cls):
        return cls.query.all()


    @classmethod
    def delete(cls, id):

        task = cls.query.get(id)

        if not task:
            raise NoResultFound

        db.session.delete(task)
        db.session.commit()