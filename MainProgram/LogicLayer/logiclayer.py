import csv
import datetime
from DataLayer.datalayer import Database

class Flight():
    distance = None
    
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

    def checkTimeAvailable(self, is_time_avail):
        self.reserved = is_time_avail
        if self.reserved == False:
            return True

    def createFlight(self):
        ''' 
        Þarf að gera fall sem býr til nýtt flug með öllum upplýsingunum sem það tekur inn í __init__() 
        það væri best að láta þetta fall sækja csv frá Datalayer. Fyrst samt að prufa í testskjali.

        '''

    def updateFlight(self):
        ''' Geyma '''
        pass


class Employee:
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
        emp = {'ssn': self.ssn, 'firstname': self.firstname, 'lastname': self.lastname, 'role': self.role , 'rank': self.rank, 'licence': self.licence, 'address': self.address, 'mobile': self.mobile, 'email': self.email_str, 'working': self.working, 'arriving': self.arriving}       
        storing = Database(2,emp)
        storing.create_data()

    def updatePhonenumber(self):
        pass

    def updateMobile(self):
        pass

    def updateEmail(self):
        pass

    def updateAddress(self):
        pass

    def updateTile(self):
        pass


class flight_attendant(Employee):
    def __init__ (self, supervisor, airplane_type):
        self.supervisor = supervisor
        self.airplane_type = airplane_type
        self.distance = Flight.distance
        
    def set_supervisor(self):
        '''
        Þetta fall á að beyta einu gildi á flight attendant starfsmanni. 
        Semsagt að geta breytt úr Supervisor = False yfir í Supervisor = True.
        Þarf að sækja csv frá Datalayer.
        '''
        pass


class Voyage(Flight):
    def __init__(self, destination, date_from_iceland, date_back_to_iceland, pilot_captain, pilot_copilot, flight_attendant_supervisor, flight_attendant):
        self.destination = destination
        self.date_from_iceland = date_from_iceland
        self.date_back_to_iceland = date_back_to_iceland
        self.pilot_captain = pilot_captain
        self.pilot_copilot = pilot_copilot
        self.flight_attendant_supervisor = flight_attendant_supervisor
        self.flight_attendant = flight_attendant
    
    def store_voyage(self):
        voy = {'destination': self.destination, 'date_from_iceland': self.date_from_iceland, 'date_back_to_iceland': self.date_back_to_iceland,'pilot_captain': self.pilot_captain ,'pilot_copilot': self.pilot_copilot,'flight_attendant_supervisor': self.flight_attendant_supervisor,'flight_attendant': self.flight_attendant}       
        storing = Database(6,voy)
        storing.create_data()
    
    def update_fight_number(self):
        pass


class Destination:
    def __init__(self, short, location, airport, flighttime, distance, emergencycontact, emergencynumber):
        self.short = short
        self.location = location
        self.airport = airport
        self.flighttime = flighttime
        self.distance = distance
        self.emergencycontact = emergencycontact
        self.emergencynumber = emergencynumber
    
    def store_destination(self):
        dest_dict = {'id': self.short, 'location': self.location, 'airport': self.airport,'flighttime': self.flighttime,'distance': self.distance,'contact': self.emergencycontact,'number': self.emergencynumber}
        storing = Database(3,dest_dict)
        storing.create_data()

    def updateEmergencyContact(self):
        pass


class Aircraft():
    def __init__(self, aircraft_type, num_seats, manufacturer, name_of_aircraft):
        self.aircraft_type = aircraft_type
        self.num_seats = num_seats
        self.manufacturer = manufacturer
        self.name_of_aircraft = name_of_aircraft
        
    def store_aircraft(self):
        airc = {'aircraft_type': self.aircraft_type, 'num_seats': self.num_seats, 'manufacturer': self.manufacturer,'name_of_aircraft': self.name_of_aircraft}       
        storing = Database(1,airc)
        storing.create_data()

    def save_aircraft(self):
        pass


class Pilot(Employee):
    def __init__(self, aircraft, flight_license, aircraft_type, captain):
        self.aircraft = aircraft
        self.flight_license = flight_license
        self.aircraft_type = aircraft_type
        self.captain = captain

    def update_licence(self):
        pass

    def set_airplane(self):
        pass

    def update_aiplane_type(self):
        pass
    

class Get_Data:
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
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        return self.datalist

    def get_specific_emp(self):
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
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["role"] == "Pilot":
                templist.append(row)
        return templist

    def get_flightattendants(self):
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["role"] == "Cabincrew":
                templist.append(row)
        return templist

    def get_destinations(self):
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        return self.datalist

    def get_emp_not_working(self):
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["working"] == "Not Working":
                templist.append(row)
        return templist

    def get_emp_working(self):
        templist = []
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["working"] == "Working":
                templist.append(row)
        return templist

    def get_emp_work_summary(self):
        pass

    def get_aircraft_pilot_licence(self):
        pass

    def get_voyage(self):
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        return self.datalist

    def get_voyage_emp_week(self):
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

    def get_voyage_ID(self):
        pass

    def get_pilots_from_airtype(self):
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

    def get_nan_aircrafts(self):
        pass

    def get_checker(self):
        checker = False
        self.date = datetime.datetime.fromisoformat(self.date)
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            temptime = datetime.datetime.fromisoformat(row['date_from_iceland'])
            if row[self.key] == self.name and temptime.date() == self.date.date():
                checker = True
        
        return checker