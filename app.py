from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['DATABASE'] = 'ENTERFILEPATHTORESEVATIONSDB'

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

# Route to handle admin login
@app.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    
    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Check admin credentials
    cursor.execute("SELECT * FROM admins WHERE username = ? AND password = ?", (username, password))
    admin = cursor.fetchone()
    
    conn.close()

    if admin:
        return "SEATINGCHART HERE"
    else:
        return "Invalid username or password. Please try again."

# Route to handle form submission and add a new reservation to the database
@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    passenger_name = request.form['passenger_name']
    seat_row = request.form['seat_row']
    seat_column = request.form['seat_column']
    e_ticket_number = request.form['e_ticket_number']

    # Connect to the database
    conn = sqlite3.connect('/reservations.db')
    c = conn.cursor()

    c.execute("INSERT INTO reservations (passengerName, seatRow, seatColumn, eTicketNumber) VALUES (?, ?, ?, ?)",
              (passenger_name, seat_row, seat_column, e_ticket_number))

    conn.commit()
    conn.close()

    return redirect(url_for('admin_dashboard'))
 
if __name__ == '__main__':
    app.run(host="0.0.0.0")
