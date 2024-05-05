from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from logan_methods import loganMethods

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
    lm = loganMethods()
    seating = lm.seatingChart()
    return render_template('reserve.html', rows=seating)

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
                lm = loganMethods()
                seating = lm.seatingChart()
                return render_template('admin.html', rows=seating, sales_total=lm.salesTotal(seating))
            else:
                message = "Invalid username or password."
                return render_template('admin-login.html', message=message)
    else:
        return render_template('index.html')

@app.route('/add_reservation', methods=['POST'])
def add_reservation():
    lm = loganMethods()
    seating = lm.seatingChart()
    rows=[]
    cols=[]
    count = 0
    isTaken = False

    passenger_name = request.form['first']
    seat_row = str(int(request.form['row']) - 1)
    seat_column = str(int(request.form['column']) - 1)
    e_ticket_number = lm.ticketNum(request.form['first'])

    if passenger_name == "":
        return render_template('reserve.html', rows=seating, message="Please enter a first name.")

    # Connect to the database
    conn = sqlite3.connect('dbs/reservations.db')
    c = conn.cursor()
               
    c.execute("SELECT seatRow FROM reservations")
    for x in c.fetchall():
        rows.append(x[0])
    print(rows)
    c.execute("SELECT seatColumn FROM reservations")
    for x in c.fetchall():
        cols.append(x[0])
    print(cols)

    for x in rows:
        if x == int(seat_row):
            if cols[count] == int(seat_column):
                isTaken = True
                print('test')
        count+=1

    if isTaken == True:
        conn.close()
        return render_template('reserve.html', rows=seating,message="Seat is taken, please choose another.")
    else:
        c.execute("INSERT INTO reservations (passengerName, seatRow, seatColumn, eTicketNumber) VALUES (?, ?, ?, ?)",
        (passenger_name, seat_row, seat_column, e_ticket_number))
        conn.commit()
        conn.close()

    seating = lm.seatingChart()

    message = "Reservation was successful! Your reservation number is " + e_ticket_number
    return render_template('reserve.html', rows=seating, message=message)

if __name__ == '__main__':
    app.run(port=5000)
