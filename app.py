from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/admin-login')
def login():
    return render_template('admin-login.html')

@app.route('/reserve')
def reserve():
    return render_template('reserve.html')

def admin_check(username, password):
    db_path = 'dbs/reservations.db'
    conn = sqlite3.connect(db_path)
    result = conn.execute("SELECT * FROM admins WHERE username =? AND password =?", (username, password)).fetchone()
    conn.close() 
    return result

@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        menu_option = request.form.get('menu')
        if menu_option:
            if menu_option == "/admin-login":
                return redirect(url_for('login'))
            elif menu_option == "/reserve":
                return redirect(url_for('reserve'))
            else:
                return "Invalid menu option", 400
        else:
            username = request.form.get('username')
            password = request.form.get('password')
            if admin_check(username, password):
                return render_template('admin.html')
            else:
                message = "Invalid username or password."
                return render_template('admin-login.html', message=message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000)