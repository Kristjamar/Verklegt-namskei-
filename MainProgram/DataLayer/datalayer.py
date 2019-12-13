import csv
import shutil
from tempfile import NamedTemporaryFile

Aircraft = 1
Crew = 2
Destinations = 3
PastFlights = 4
UpcomingFlights = 5
Voyage = 6

class Database():

    def __init__(self, request, append_dict={}):
        ''' Main function is that init make the "filename" what you need it to be when selecting from the menu '''
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
            self.fieldnames = ['ssn', 'firstname', 'lastname', 'role', 'rank', 'licence', 'address', 'mobile', 'email', 'working', 'arriving']
            self.rowvalue = "ssn"
        elif self.request == Destinations:
            self.filename = "./CSV/Destinations.csv"
            self.fieldnames = ['id', 'location', 'airport', 'flighttime', 'distance', 'contact', 'number']
        elif self.request == PastFlights:
            self.filename = "./CSV/PastFlights.csv"
        elif self.request == UpcomingFlights:
            self.filename = "./CSV/UpcomingFlights.csv"
        elif self.request == Voyage:
            self.filename = "./CSV/Voyage.csv"
            self.fieldnames = ['date_from_iceland','destination','date_back_to_iceland','pilot_captain','pilot_copilot','flight_attendant_supervisor','flight_attendant']
            self.rowvalue = "date_from_iceland"
        
    def get_data(self):
        ''' Gets the information from the csv files and returns a list of dictionaries '''               
        try:
            with open(self.filename, 'r', newline='') as self.csvfile:
                self.reader = csv.reader(self.csvfile, skipinitialspace=True)
                header = next(self.reader)
                listcreator = [dict(zip(header, map(str, row))) for row in self.reader]
                return listcreator

        except FileNotFoundError:
            print("Filename {} not found!".format(self.filename))

    def create_data(self):
        ''' Appends new data to the csv file with dictwriter '''                
        try:
            with open(self.filename, 'a', newline='') as self.csvfile:
                writer = csv.DictWriter(self.csvfile, fieldnames=self.fieldnames)
                writer.writerow(self.append_dict)

        except FileNotFoundError:
            print("Filename {} not found!".format(self.filename))

    def update_data(self):
        ''' 
        Updates data in csv file with dictwriter. Creates a new temporary file
        with the updated data and overwrites the old one.
        ''' 
        tempfile = NamedTemporaryFile(mode='w',newline='', delete=False)
        with open(self.filename, 'r', newline='') as self.csvfile, tempfile:
            reader = csv.DictReader(self.csvfile, fieldnames=self.fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=self.fieldnames)
    
            for row in reader:
                if row[self.rowvalue] == self.append_dict[self.rowvalue]:
                    writer.writerow(self.append_dict)
                else:
                    writer.writerow(row)

        shutil.move(tempfile.name, self.filename)