# routes/example_routes.py
from flask import Blueprint
import json
registarion = Blueprint('example', __name__)

@registarion.route('/')
def home():
    return 'Welcome to the Home Page!'

@registarion.route('/about')
def about():
    return 'This is the About Page.'


from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# File to store user data
USERS_FILE = 'users.json'

def load_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = load_users()
        name = request.form['name']
        
        if name in users:
            flash('Username already exists')
            return redirect(url_for('register'))
        
        user_data = {
            'address': generate_password_hash(request.form['address']),
            'gender': request.form['gender'],
            'state': generate_password_hash(request.form['state']),
            'dob': generate_password_hash(request.form['dob']),
            'pincode': generate_password_hash(request.form['pincode']),
            'email': request.form['email'],
            'father_name': request.form['father_name'],
            'city': request.form['city'],
            'password': generate_password_hash(request.form['password'])
        }
        
        users[name] = user_data
        save_users(users)
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register1.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        name = request.form['name']
        password = request.form['password']
        
        if name not in users:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        if check_password_hash(users[name]['password'], password):
            session['username'] = name
            flash('Logged in successfully!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if 'username' not in session:
        return redirect(url_for('chatbot'))

    return render_template('chatbot.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully!')
    return redirect(url_for('home'))
