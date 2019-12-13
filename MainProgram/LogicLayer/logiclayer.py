import csv
import datetime
from DataLayer.datalayer import Database

class Flight():
    ''' Parent of Voyage, helps create new flights and voyages. '''
    distance = None
    
    #Constants for distance
    longyearbyean = 4
    nuuk = 3
    kulusuk = 2
    thorshavn = 1
    tingwall = 2
    
    def __init__(self, pilots, flighttype, flightattendants, numseats, flightnum, airplanetype, date, flightreserved, given_distance):
        self.pilots = pilots
        self.flighttype_str = flighttype
        self.flightattendants = flightattendants
        self.numseats = numseats
        self.flightnum = flightnum
        self.airplanetype = airplanetype
        self.date = date
        self.reserved = flightreserved
        Flight.distance = given_distance


class Employee:
    ''' Class for handling employees '''
    def __init__(self, ssn, firstname, lastname, rank, role, licence, address, mobile):
        self.firstname = firstname
        self.lastname = lastname
        self.ssn = ssn
        self.rank = rank
        self.role = role
        self.licence = licence
        self.mobile = mobile
        self.email_str = firstname + lastname + "@nan.is"
        self.address = address
        self.working = "Not Working"
        self.arriving = "N/A"

    def save_employee(self):
        #Append new employee
        emp = {'ssn': self.ssn, 'firstname': self.firstname, 'lastname': self.lastname, 'role': self.role , 'rank': self.rank, 'licence': self.licence, 'address': self.address, 'mobile': self.mobile, 'email': self.email_str, 'working': self.working, 'arriving': self.arriving}       
        storing = Database(2,emp)
        storing.create_data()

    def update_employee(self):
        #Update a employee
        emp = {'ssn': self.ssn, 'firstname': self.firstname, 'lastname': self.lastname, 'role': self.role , 'rank': self.rank, 'licence': self.licence, 'address': self.address, 'mobile': self.mobile, 'email': self.email_str, 'working': self.working, 'arriving': self.arriving}
        update = Database(2,emp)
        update.update_data()


class Voyage(Flight):
    ''' A child of flight. Class for handling voyages. '''
    def __init__(self, date_from_iceland, destination, date_back_to_iceland, pilot_captain, pilot_copilot, flight_attendant_supervisor, flight_attendant):
        self.destination = destination
        self.date_from_iceland = date_from_iceland
        self.date_back_to_iceland = date_back_to_iceland
        self.pilot_captain = pilot_captain
        self.pilot_copilot = pilot_copilot
        self.flight_attendant_supervisor = flight_attendant_supervisor
        self.flight_attendant = flight_attendant
    
    def store_voyage(self):
        #Creates new voyages
        voy = {'date_from_iceland': self.date_from_iceland, 'destination': self.destination, 'date_back_to_iceland': self.date_back_to_iceland,'pilot_captain': self.pilot_captain ,'pilot_copilot': self.pilot_copilot,'flight_attendant_supervisor': self.flight_attendant_supervisor,'flight_attendant': self.flight_attendant}       
        storing = Database(6,voy)
        storing.create_data()

    def update_voyage(self):
        #Updates voyages
        voy = {'destination': self.destination, 'date_from_iceland': self.date_from_iceland, 'date_back_to_iceland': self.date_back_to_iceland,'pilot_captain': self.pilot_captain ,'pilot_copilot': self.pilot_copilot,'flight_attendant_supervisor': self.flight_attendant_supervisor,'flight_attendant': self.flight_attendant}      
        storing = Database(6,voy)
        storing.update_data()  


class Destination:
    ''' Class for handling destinations '''
    def __init__(self, short, location, airport, flighttime, distance, emergencycontact, emergencynumber):
        self.short = short
        self.location = location
        self.airport = airport
        self.flighttime = flighttime
        self.distance = distance
        self.emergencycontact = emergencycontact
        self.emergencynumber = emergencynumber
    
    def store_destination(self):
        #Create new destination
        dest_dict = {'id': self.short, 'location': self.location, 'airport': self.airport,'flighttime': self.flighttime,'distance': self.distance,'contact': self.emergencycontact,'number': self.emergencynumber}
        storing = Database(3,dest_dict)
        storing.create_data()


class Aircraft():
    ''' Class to handle aircrafts '''
    def __init__(self, aircraft_type, num_seats, manufacturer, name_of_aircraft):
        self.aircraft_type = aircraft_type
        self.num_seats = num_seats
        self.manufacturer = manufacturer
        self.name_of_aircraft = name_of_aircraft
        
    def store_aircraft(self):
        #Creates a new aircraft
        airc = {'aircraft_type': self.aircraft_type, 'num_seats': self.num_seats, 'manufacturer': self.manufacturer,'name_of_aircraft': self.name_of_aircraft}       
        storing = Database(1,airc)
        storing.create_data()
    

class Get_Data:
    ''' Handles all listing data. '''
    def __init__(self, request, SSN=None, licence=None, name=None, date=None, key=None):
        self.SSN = SSN
        self.datalist = None
        self.request = request
        self.DBsmith = None
        self.licence = licence
        self.name = name
        self.date = date
        if key == 1:
            self.key = "pilot_captain"
        elif key == 2:
            self.key = "pilot_copilot"
        elif key == 3:
            self.key = "flight_attendant_supervisor"
        elif key ==4:
            self.key = "flight_attendant"

    def get_emp_list(self):
        #List employees
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        return self.datalist

    def get_specific_emp(self):
        #List specific employee by SSN
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["ssn"] == self.SSN:
                templist.append(row)
        if templist:
            return templist
        else:
            return False

    def get_pilots(self):
        #Lists pilots
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["role"] == "Pilot":
                templist.append(row)
        return templist

    def get_flightattendants(self):
        #Lists flight attendants
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["role"] == "Cabincrew":
                templist.append(row)
        return templist

    def get_destinations(self):
        #List destination
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        return self.datalist

    def get_emp_not_working(self):
        #List employees that are not working
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["working"] == "Not Working":
                templist.append(row)
        return templist

    def get_emp_working(self):
        #List employees that are working
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["working"] == "Working":
                templist.append(row)
        return templist

    def get_voyage(self):
        #List voyages
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        return self.datalist

    def get_voyage_emp_week(self):
        #List voyages flown by a employee in a certain week.
        templist = []
        finallist = []
        self.date = datetime.datetime.fromisoformat(self.date)
        timedelta = datetime.timedelta(days=1)
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if (row["pilot_captain"] == self.name) or (row["pilot_copilot"] == self.name) or (row["flight_attendant_supervisor"] == self.name) or (row["flight_attendant"] == self.name):
                templist.append(row)
        for _ in range(1,8):
            for row in templist:
                temptime = datetime.datetime.fromisoformat(row['date_from_iceland'])
                if temptime.date() == (self.date.date()):
                    finallist.append(row)
            self.date = self.date + timedelta

        if finallist:
            return finallist
        else:
            return False

    def get_voyage_week(self):
        #Lists voyages in a certain week
        finallist = []
        self.date = datetime.datetime.fromisoformat(self.date)
        timedelta = datetime.timedelta(days=1)
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for _ in range(1,8):
            for row in self.datalist:
                temptime = datetime.datetime.fromisoformat(row['date_from_iceland'])
                if temptime.date() == (self.date.date()):
                    finallist.append(row)
            self.date = self.date + timedelta
        if finallist:
            return finallist
        else:
            return False

    def get_voyage_day(self):
        #List voyages flown on a day
        finallist = []
        self.date = datetime.datetime.fromisoformat(self.date)
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            temptime = datetime.datetime.fromisoformat(row['date_from_iceland'])
            if temptime.date() == (self.date.date()):
                finallist.append(row)
        if finallist:
            return finallist
        else:
            return False

    def get_pilots_from_airtype(self):
        #Lists pilots that have licence on entered aircraft
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["licence"] == self.licence:
                templist.append(row)
        if templist:
            return templist
        else:
            return False

    def get_checker(self):
        #Helper to check if employee has already flown on entered day
        checker = False
        self.date = datetime.datetime.fromisoformat(self.date)
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            temptime = datetime.datetime.fromisoformat(row['date_from_iceland'])
            if row[self.key] == self.name and temptime.date() == self.date.date():
                checker = True
        
        return checker