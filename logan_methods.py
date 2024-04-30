class loganMethods:
    def seatingChart(self, rows, cols):
        seats = [
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O'],
            ['O','O','O','O']
        ]
        count = 0

        for x in rows:
            
            seats[x][cols[count]] = 'X'
            count+=1

        return seats


    #def ticketNum():


    #def salesTotal():

