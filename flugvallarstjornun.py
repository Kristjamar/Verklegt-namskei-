Aircarft = 1
Crew = 2
Destinations = 3
PastFlights = 4
UpcommingFlights = 5
'''---------- User Interface ----------'''



'''---------- Logic Layer ----------'''
class Flight():
    def __init__(self, pilots, flighttype, flightattendants, numseats, flightnum, airplanetype, date, flightreserved, distance):
        self.pilots = pilots
        self.flighttype_str = flighttype
        self.flightattendants = flightattendants
        self.numseats = numseats
        self.flightnum = flightnum
        self.airplanetype = airplanetype
        self.date = date
        self.reserved = flightreserved
        self.distance = distance

    def checkTimeAvailable(self, is_time_avail):
        self.reserved = is_time_avail
        if self.reserved == False:
            return True

    def createFlight(self):
        pass

    def updateFlight(self):
        pass


class Employee():
    def __init__(self, firstname, lastname, socialnumber, title = "", phonenumber = 0 ,mobile = 0 ,address = ""):
        self.first = firstname
        self.last = lastname
        self.title = title
        self.socialnumber = socialnumber
        self.phonenumber = phonenumber
        self.mobile = mobile
        self.email_str = firstname + lastname + "@nan.is"
        self.address = address

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


class flight_attendant(Employee):
    def __init__ (self, supervisor, airplane_type):
        self.supervisor = supervisor
        self.airplane_type = airplane_type
        
    def set_supervisor(self):
        pass

    def set_airplane_type(self):
        pass


class voyage(Employee):
    def __init__(self, time_iceland, time_other):
        pass

    def double_distance(self):
        pass
    
    def double_time_of_arriveal(self):
        pass
    
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

    def storeFlightLength(self):
        pass
    
    def __str__(self):
        pass


class Airplane():
    def __init__(self, airplane_type, num_seats, manufacturer, name_of_airplane):
        self.airplane_type = airplane_type
        self.num_seats = num_seats
        self.manufacturer = manufacturer
        self.name_of_airplane = name_of_airplane

    def create_airplane(self):
        pass


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
'''---------- Database ----------'''
class Database():
    filename = ""
        
    def getPastFlights(self):               
        Database.filename = "PastFlights.csv"
        try:
            file_object = open(Database.filename, "w+")
            return file_object
        except FileNotFoundError:
            print("Filename {} not found!".format(Database.filename))
    

'''---------- Main ----------'''
def MainMenu():
    pass

MainMenu()