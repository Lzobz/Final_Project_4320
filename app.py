from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ENTERFILEPATHTORESEVATIONSDB'
db = SQLAlchemy(app)

class Admin(db.Model):
    username = db.Column(db.TEXT, primary_key=True)
    password = db.Column(db.TEXT, nullable=False)

@app.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    admin = Admin.query.filter_by(username=username, password=password).first()
    if admin:
        return "SEATINGCHART HERE"
    else:
        return "Invalid username or password. Please try again."

if __name__ == '__main__':
    app.run(host="0.0.0.0")
