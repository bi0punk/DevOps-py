
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
import os
import subprocess
from datetime import datetime
import time 
import socket

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username", "input type":"text", "class":"form-control",  "id":"floatingInput"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password", "input type":"password", "class":"form-control",  "id":"floatingPassword", "placeholder":"Password"})

    submit = SubmitField('Iniciar Sesión',render_kw={"class":"btn btn-outline-danger"})


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)




@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    now = datetime.today().strftime('%A, %B %d, %Y, %H:%M:%S')
    hip = socket.gethostbyname(socket.gethostname())
    hname = socket.gethostname()
    p = time.time()

    try:
        kil = os.popen('taskkill/ PID 12748 / F').read()
        #serv = subprocess.run("taskkill /F 18828", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        #serv.stdout
        pid = os.popen('wmic process get processid').read()

        name = os.popen('wmic process get description').read()
        #print(pid)
    except IndexError as e:
        print("ª")
    f = time.time()
    print(f-p)
    return render_template('dashboard.html', now = now, hname = hname, hip = hip)



@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)




#POST METHODS


@app.route('/commands', methods=['POST'])
def command():
    a = datetime.today().strftime('%A, %B %d, %Y, %H:%M:%S')
    if request.method == 'POST':
        return f'Comando ejecutado correctamente: '+str(a)


if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.82', port=5000)




