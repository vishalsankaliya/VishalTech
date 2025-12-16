from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def aboutus():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contactus():
    return render_template('contact.html')

app.run(debug=True)