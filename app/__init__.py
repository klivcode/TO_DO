# this is a factory of app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create Database globally
db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config["SECRET_KEY"]='your_secrect_key'
    app.config['SQLALCHEMY_DATABASE_URI']='sqllite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATONS']=False
    
    db.__init__(app)
    
    # blueprint register (mini app || module to know the flask)
    from app.routes.auth import auth_bp
    from app.routes.auth import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    return app