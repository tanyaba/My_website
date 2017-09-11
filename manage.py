import os
from app import create_app
from flask_script import Manager
from flask import render_template

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager=Manager(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    manager.run()

