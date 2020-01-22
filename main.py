<<<<<<< HEAD
from flask import Flask, render_template, redirect, request, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "super-secret-key"
app.config['MONGO_URI'] = 'mongodb://localhost/nt'
mongo = PyMongo(app)
=======
from flask import Flask, render_template, redirect, request
#from flask_pymongo import PyMongo

app = Flask(__name__)
#app.config['MONGO_URI'] = 'mongodb://localhost/nt'
#mongo = PyMongo(app)
>>>>>>> 68744a39a76e0d864247f4b281ec92de78d132d6


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        passw = request.form.get('pass')
<<<<<<< HEAD
        print(email)
        print(passw)
        result = mongo.db.nt.find_one({"email": email, "password": passw})
        print(result)
        if result is None:
            return render_template('login.html', i="invalid Id/Password")
        else:
            session['user'] = email
            return "Welcome "+result['name']+"!"
=======
       # result = mongo.db.nt.find_one({"passw": passw, "email": email})
>>>>>>> 68744a39a76e0d864247f4b281ec92de78d132d6
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print("in if")
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('pass')
        print(name, email, password)
        result = mongo.db.nt.insert({"name": name, "email": email, "password": password})
        print(result)
        return "Ok we got it!"
    print("h")
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
