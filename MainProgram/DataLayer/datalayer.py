import csv

Aircraft = 1
Crew = 2
Destinations = 3
PastFlights = 4
UpcomingFlights = 5


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
            self.filename = "Destiantions.csv"
        elif self.request == PastFlights:
            self.filename = "PastFlights.csv"
        elif self.request == UpcomingFlights:
            self.filename = "UpcomingFlights.csv"
        
    def get_data(self):               
        try:
            with open(self.filename, 'r', newline='') as self.csvfile:
                self.reader = csv.DictReader(self.csvfile, fieldnames=self.fieldnames)
                for row in self.reader:
                    self.datalist.append(row)
                return self.datalist
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

shit = Database(2)
shit.get_data()
print(shit)