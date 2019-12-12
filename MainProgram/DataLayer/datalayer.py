import csv

Aircraft = 1
Crew = 2
Destinations = 3
PastFlights = 4
UpcomingFlights = 5
Voyage = 6

class Database():

    def __init__(self, request, append_dict):
        self.datalist = []
        self.fieldnames = None
        self.reader = None
        self.request = request
        self.append_dict = append_dict
        if self.request == Aircraft:
            self.filename = "./CSV/Aircraft.csv"
            self.fieldnames = ['aircraft_type', 'num_seats','manufacturer','name_of_aircraft']
        elif self.request == Crew:
            self.filename = "./CSV/Crew.csv"
        elif self.request == Destinations:
            self.filename = "./CSV/Destinations.csv"
        elif self.request == PastFlights:
            self.filename = "./CSV/PastFlights.csv"
        elif self.request == UpcomingFlights:
            self.filename = "./CSV/UpcomingFlights.csv"
        elif self.request == Voyage:
            self.filename = "./CSV/Voyage.csv"
        
    def get_data(self):               
        try:
            with open(self.filename, 'r', newline='') as self.csvfile:
                self.reader = csv.reader(self.csvfile, skipinitialspace=True)
                header = next(self.reader)
                listcreator = [dict(zip(header, map(str, row))) for row in self.reader]
                return listcreator

        except FileNotFoundError:
            print("Filename {} not found!".format(self.filename))

    def create_data(self):               
        try:
            with open(self.filename, 'a', newline='') as self.csvfile:
                writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
                writer.writerow(self.append_dict)

        except FileNotFoundError:
            print("Filename {} not found!".format(self.filename))