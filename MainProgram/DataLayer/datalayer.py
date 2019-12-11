import csv

Aircraft = 1
Crew = 2
Destinations = 3
PastFlights = 4
UpcomingFlights = 5
Voyage = 6

class Database():

    def __init__(self, request):
        self.datalist = []
        self.fieldnames = None
        self.reader = None
        self.request = request
        if self.request == Aircraft:
            self.filename = "Aircraft.csv"
        elif self.request == Crew:
            self.filename = "Crew.csv"
        elif self.request == Destinations:
            self.filename = "Destinations.csv"
        elif self.request == PastFlights:
            self.filename = "PastFlights.csv"
        elif self.request == UpcomingFlights:
            self.filename = "UpcomingFlights.csv"
        elif self.request == Voyage:
            self.filename = "Voyage.csv"
        
    def get_data(self):               
        try:
            with open(self.filename, 'r', newline='') as self.csvfile:
                self.reader = csv.reader(self.csvfile, skipinitialspace=True)
                header = next(self.reader)
                listcreator = [dict(zip(header, map(str, row))) for row in self.reader]
                return listcreator

        except FileNotFoundError:
            print("Filename {} not found!".format(self.filename))

    def ch_upd_data(self):               
        try:
            with open(self.filename, 'w+', newline='') as self.csvfile:
                self.writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
        except FileNotFoundError:
            print("Filename {} not found!".format(self.filename))

    def __str__(self):
        return "{}".format(self.datalist)
