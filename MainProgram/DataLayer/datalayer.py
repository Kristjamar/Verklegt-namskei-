Airplane = 1
Crew = 2
Destinations = 3
PastFlights = 4
UpcommingFlights = 5

class Database():

    def __init__(self, request):
        self.file_object = None
        self.request = request
        if self.request == Airplane:
            self.filename = "Airplane.csv"
        elif self.request == Crew:
            self.filename = "Crew.csv"
        elif self.request == Destinations:
            self.filename = "Destiantions.csv"
        elif self.request == PastFlights:
            self.filename = "PastFlights.csv"
        elif self.request == UpcommingFlights:
            self.filename = "UpcommingFlights.csv"
        
    def get_data(self):               
        try:
            self.file_object = open(self.filename, "r")
        except FileNotFoundError:
            print("Filename {} not found!".format(self.filename))

    def ch_upd_data(self):               
        try:
            self.file_object = open(self.filename, "w+")
        except FileNotFoundError:
            print("Filename {} not found!".format(self.filename))

    def returning_date(self):
        datalist = []
        for line in self.file_object:
            datalist.append(line.split(","))
        return datalist