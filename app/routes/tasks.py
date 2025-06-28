from flask import Flask, Blueprint,redirect,render_template,flash,url_for,session,request
from app import db

from app.models import Task

tasks_bp=Blueprint('tasks',__name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    #fetch
    tasks=Task.query_all()
    return render_template('tasks.html', tasks=tasks)


@tasks_bp.route("/add",methods=['GET',"POST"])
def add_task():
    if 'user' not in session:
        return redirect(url_for("auth.login"))
    title=request.form.get('title')
    if title:
        new_task=Task(title=title,status='Pending')
        db.session.add(new_task)
        db.session.commit()
        
        
    return redirect(url_for("tasks.view_task"))


@tasks_bp.route("/toggle/<int:task_id", methods=["POST"])
def toggle_status(task_id):
    
    