from flask import Blueprint,render_template,redirect,request,url_for,flash,session
from app.models import User
from app import db

auth_bp=Blueprint('auth',__name__)
tasks_bp = Blueprint('tasks', __name__)

USER_CREDENTIALS={
    'username':'admin',
    'password':'klivcode12'
}

@auth_bp.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user']=username
            flash('Login Successfull','success')
            return redirect(url_for('tasks.view_tasks'))
            
        else:
            flash("Invalid Username and Password",'Try Again')
    return render_template("login.html")


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)

    flash("Log out",'info')
    return redirect(url_for("auth.login"))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists. Please choose another.', 'danger')
            return redirect(url_for('auth.register'))
        
        # Create new user
        new_user = User(username=username)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        session['user']=username
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('tasks.view_tasks'))
    
    return render_template('register.html')
