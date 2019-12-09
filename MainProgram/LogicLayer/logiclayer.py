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
    def __init__(self, firstname, lastname, ssn, title, phonenumber, mobile ,address):
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
         emp = {'first_name': self.firstname, 'last_name': self.lastname, 'SSN': self.ssn,'title': self.title ,'phone_number': self.phonenumber,'mobile': self.mobile,'email': self.email_str,'address': self.address}       
         return emp

    def save_employee(self):
            with open('employeetest.csv', 'a', newline='') as csvfile:
                    fieldnames = ['first_name', 'last_name','SSN','title','phone_number','mobile','email','address']
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


class Destination():
    def __init__(self,distance = 0.0,city = "", country = "", emergencycontact = ""):
        self.distance = distance
        self.city = city
        self.country = country
        self.emergencycontact = emergencycontact
    
    def updateEmergencyContact(self):
        pass
    
    def __str__(self):
        pass


class Aircraft():
    def __init__(self, aircraft_type, num_seats, manufacturer, name_of_aircraft):
        self.aircraft_type = aircraft_type
        self.num_seats = num_seats
        self.manufacturer = manufacturer
        self.name_of_aircraft = name_of_aircraft

    def New_aircraft():
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
    

class Get_Data():

    def __init__(self, request):
        self.datalist = None
        self.request = request
        self.DBsmith = None

    def get_emp_list(self):
        ''' Ignore the Error on Database please. To be fixed. - Haffi'''
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        [print(row) for row in self.datalist]

    def get_specific_emp(self):
        self.DBsmith = Database(self.request)
        self.datalist = self.DBsmith.get_data()
        for row in self.datalist:
            if row["ssn"] == self.SSH:
                return row
        return False

    def get_pilots(self):
        pass

    def get_flightattendants(self):
        pass

    def get_voyage_day_n_week(self):
        pass

    def get_destinations(self):
        pass

    def get_emp_not_working(self):
        pass

    def get_emp_working(self):
        pass

    def get_emp_destination(self):
        pass

    def get_emp_work_summary(self):
        pass

    def get_aircraft_pilot_licence(self):
        pass

    def get_voyage_status(self):
        pass

    def get_voyage_ID(self):
        pass

    def get_pilots_from_airtype(self):
        pass

    def get_nan_aircrafts(self):
        pass