# python class which represents the table to database
from app import db

#Entity name is Task
class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    status=db.Column(db.String(20), default='Pending')
    

    