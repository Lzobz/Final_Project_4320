from flask import Flask, render_template, request
from logan_methods import loganMethods

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET', 'POST'])
def main():
    lm = loganMethods()
    rows = [0,0,2,3,4,5,8,9,11]
    cols = [2,1,2,0,3,1,2,3,0]
    seating = lm.seatingChart(rows, cols)
    name = "Alice"

    return render_template('index.html', 
        row1=seating[0],
        row2=seating[1],
        row3=seating[2],
        row4=seating[3],
        row5=seating[4],
        row6=seating[5],
        row7=seating[6],
        row8=seating[7],
        row9=seating[8],
        row10=seating[9],
        row11=seating[10],
        row12=seating[11],
        eticket=lm.ticketNum(name),
        totalSales=lm.salesTotal(seating)
        )

if __name__ == '__main__':
    app.run(port=5000)