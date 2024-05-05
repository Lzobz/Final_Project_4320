import sqlite3

class loganMethods:
    def seatingChart(self):
        seats = [['O','O','O','O'] for row in range(12)]
        count = 0
        rows=[]
        cols=[]
        
        conn = sqlite3.connect('dbs/reservations.db')
        c = conn.cursor()
        c.execute("SELECT seatRow FROM reservations")
        for x in c.fetchall():
            rows.append(x[0])

        c.execute("SELECT seatColumn FROM reservations")
        for x in c.fetchall():
            cols.append(x[0])
        conn.close()

        for x in rows:          
            seats[x][cols[count]] = 'X'
            count+=1

        return seats
    
    def ticketNum(self, name):
        ticket = ""
        mix = "INFOTC4320"

        if len(name) >= len(mix):
            for x in range(len(name)):
                ticket += name[x]
                if x <= len(mix):
                    ticket += mix[x]
        else:
            for x in range(len(mix)):
                if x < len(name):
                    ticket += name[x]
                ticket += mix[x]

        return ticket

    def salesTotal(self, seats):
        cost_matrix = [100, 75, 50, 100]
        total = 0

        for x in seats:
            count = 0
            for y in x:
                if y == 'X':
                    total += cost_matrix[count]
                count+=1

        return total

