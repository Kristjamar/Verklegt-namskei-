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
    def __init__(self, firstname, lastname, ssn, title, phonenumber, mobile, address, working="no"):
        self.firstname = firstname
        self.lastname = lastname
        self.ssn = ssn
        self.title = title
        self.phonenumber = phonenumber
        self.mobile = mobile
        self.email_str = firstname + lastname + "@nan.is"
        self.address = address

    def createEmployee(self):
        ''' 
        Þarf að gera fall sem býr til nýjan Employee með öllum upplýsingunum sem það tekur inn í __init__() 
        það væri best að láta þetta fall sækja csv frá Datalayer. Fyrst samt að prufa í testskjali.

        '''
        pass

    def store_employee(self):
         emp = {'first_name': self.firstname, 'last_name': self.lastname, 'SSN': self.ssn,'title': self.title ,'phone_number': self.phonenumber,'mobile': self.mobile,'email': self.email_str,'address': self.address, 'working': 'no'}       
         return emp

    def save_employee(self):
            with open('employeetest.csv', 'a', newline='') as csvfile:
                    fieldnames = ['first_name', 'last_name','SSN','title','phone_number','mobile','email','address','working']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    writer.writerow(Employee.store_employee(self))

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

    def __str__(self):
        pass

# def Make_and_save_employee():
#     #Makes employee from user input and saves it in a csv file, the save function will be moved later.
#     emp_str = New_employee()
#     firstname, lastname, ssn, title , phonenumber, mobile, address = emp_str
#     emp_1 = Employee(firstname, lastname, ssn, title , phonenumber, mobile, address)
    
#     emp_1.save_employee()


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


class voyage(Flight):
    def __init__(self, time_iceland, time_other):
        ## self.voydis = Flight.distance
        self.voydis = 100
        self.time_iceland = time_iceland
        self.time_other = time_other

    def double_distance(self):
        self.voydis += self.voydis
    
    def time_of_arrival(self):
        '''
        Sýna hvenær flugvéling lendir á íslandi eftir að hafa flogið til útlanda og svo aftur heim.
        self.time_iceland er gefinn tími þegar flugvélinn tekur af stað. self.time_other er tíminn á tímabeltinu úti.
        Það þarf að reikna þetta úr frá föstunum sem eru uppi.
        '''
        self.time_iceland += Flight.kulusuk
        self.time_iceland += Flight.nuuk
        self.time_iceland += Flight.thorshavn
        self.time_iceland += Flight.tingwall
        self.time_iceland += Flight.longyearbyean
    
    def check_pilot_licence(self):
        pass
    
    def check_emp_day_voyage(self):
        pass
    
    def store_voyage(self):
        pass
    
    def update_fight_number(self):
        pass


class Destination:
    def __init__(self, country, city, airport, flighttime, distance, emergencycontact, emergencynumber):
        self.country = country
        self.city = city
        self.airport = airport
        self.flighttime = flighttime
        self.distance = distance
        self.emergencycontact = emergencycontact
        self.emergencynumber = emergencynumber

    def New_destination():
        country = input("country: ")
        city = input("city: ")
        airport = input("airport: ")
        flighttime = input("flighttime: ")
        distance = input("distance: ")
        emergencycontact = input("emergencycontact: ")
        emergencynumber = input("emergencynumber: ")

        dest_str = country, city, airport, flighttime, distance, emergencycontact, emergencynumber
        return dest_str  
    
    def updateEmergencyContact(self):
        pass
    
    def __str__(self):
        pass

    def store_destination(self):
         dest = {'country': self.country, 'city': self.city, 'airport': self.airport,'flighttime': self.flighttime, 'distance': self.distance, 'emergencycontact': self.emergencycontact, 'emergencynumber': self.emergencynumber}       
         return dest

    def save_destination(self):
            with open('employeetest.csv', 'a', newline='') as csvfile:
                    fieldnames = ['country', 'city','airport','flighttime', 'distance', 'emergencycontact', 'emergencynumber']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    writer.writerow(Destination.store_destination(self))


class Aircraft():
    def __init__(self, aircraft_type, num_seats, manufacturer, name_of_aircraft):
        self.aircraft_type = aircraft_type
        self.num_seats = num_seats
        self.manufacturer = manufacturer
        self.name_of_aircraft = name_of_aircraft

    def New_aircraft(self):
        ''' 
    Þarf að gera fall sem býr til nýja Flugvél með öllum upplýsingunum sem það tekur inn í __init__() 
    það væri best að láta þetta fall sækja csv frá Datalayer. Fyrst samt að prufa í testskjali.

    '''
        aircraft_type = input("aircraft_type: ")
        num_seats = input("num_seats: ")
        manufacturer = input("manufacturer: ")
        name_of_aircraft = input("name_of_aircraft: ")
        
        airc_str = aircraft_type, num_seats, manufacturer, name_of_aircraft
        #return aircraft_type, num_seats, manufacturer, name_of_aircraft
        return airc_str
        
    def store_aircraft(self):
         airc = {'aircraft_type': self.aircraft_type, 'num_seats': self.num_seats, 'manufacturer': self.manufacturer,'name_of_aircraft': self.name_of_aircraft}       
         return airc

    def __str__(self):
        pass

    def save_aircraft(self):
            with open('employeetest.csv', 'a', newline='') as csvfile:
                    fieldnames = ['aircraft_type', 'num_seats','manufacturer','name_of_aircraft']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    writer.writerow(Aircraft.store_aircraft(self))


class Pilot(Employee):
    def __init__(self, airplane, flight_license, airplane_type, captain):
        self.airplane = airplane
        self.fligh_license = flight_license
        self.airplane_type = airplane_type
        self.captain = captain

    def update_licence(self):
        pass

    def set_airplane(self):
        pass

    def update_aiplane_type(self):
        pass
    

class Get_Data:
    def __init__(self, request, SSN=None, licence=None):
        self.SSN = SSN
        self.datalist = None
        self.request = request
        self.DBsmith = None
        self.licence = licence

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
        pass

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