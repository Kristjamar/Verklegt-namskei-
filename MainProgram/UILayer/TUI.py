from LogicLayer.logiclayer import Employee , Aircraft, Get_Data, Destination, Voyage

MAINMENU = "m"
BACK = "b"
QUIT = "q"
CANCEL = "c"

class Menu:
    ''' A class to build menus '''
    def __init__(self, title, how_many_options,option1, option2, option3, option4, option5, option6, option7, option8, option9,option10):
        
        self.title = title
        self.how_many_options = how_many_options
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.option5 = option5
        self.option6 = option6
        self.option7 = option7
        self.option8 = option8
        self.option9 = option9
        self.option10 = option10

    def build_title(self):
        ''' Title builder, creates the appropriate title. '''
        print("########################################")
        print("##{:^36}##".format(self.title))
        print("########################################")
        print("#                                      #")
        
    def build_menu(self):
        ''' Menu builder, this makes use of the constats below and the formating makes this an easy way to change the options the menu needs '''
        print("# 1.{:34} #".format(self.option1))
        print("# 2.{:34} #".format(self.option2))
        if self.how_many_options >= 3:
            print("# 3.{:34} #".format(self.option3))
        if self.how_many_options >= 4:
            print("# 4.{:34} #".format(self.option4))
        if self.how_many_options >= 5:
            print("# 5.{:34} #".format(self.option5))
        if self.how_many_options >= 6:
            print("# 6.{:34} #".format(self.option6))
        if self.how_many_options >= 7:
            print("# 7.{:34} #".format(self.option7))
        if self.how_many_options >= 8:
            print("# 8.{:34} #".format(self.option8))
        if self.how_many_options == 9:
            print("# 9.{:34} #".format(self.option9))
        if self.how_many_options == 9:
            print("# 10.{:34} #".format(self.option10))
        print("#                                      #")
        print("########################################")
        if self.title == "Main Menu":
            print("   [Q]uit")
        elif self.how_many_options <=4:
            print('   [B]ack       [M]ain_menu')
        elif self.how_many_options >=9:
            #Ccancel = "[Enter 'C' to cancel]"
            print('{:^40}'.format("[Enter 'C' to cancel]"))
        return ""

#Constants for menu building
main_menu = Menu("Main Menu", 3, "Register", "Information", "Update info","","","","","","","")
register_menu = Menu("Register", 4, "Register employee", "Register destination", "Register voyage", "Register aircraft","","","","","","")
listing_menu = Menu("Information", 4, "Show employees", "Show destinations", "Show voyages", "Show aircraft","","","","","","")
update_menu = Menu("Update info", 2, "Update employee", "Update voyages", "", "","","","","","","")
register_emp_menu = Menu("Register Employee", 10, "SSN:(0808693369)","First name:(Jón)", "Last name:(Jónsson)",  "Role: (Pilot)","Rank: (Captain)","Licence: (NAFokkerF100/(N/A))","Address:(Bankastræti 5)", "Mobile:(5812345)","Email:(Jónjónsson@nan.is)","Address:(Bankastræti 5)")

def first_menu():
    ''' Main Menu, sends the user to: Register Menu, Listing Menu or Update Menu '''
    main_menu.build_title()
    main_menu.build_menu()
    print()
    user_input = input("Choose an option: ")
    
    if user_input == "1":
        Reg_menu()
    elif user_input == "2":
        get_menu()
    elif user_input == "3":
        upd_menu()
    elif user_input == QUIT:
        exit
    else:
        print("Invalid input")
        first_menu()
def upd_menu():
    ''' Menu used to update already created data. Sends the user too '''
    update_menu.build_title()
    update_menu.build_menu()
    print("")
    user_input = input("Choose an option: ")
    if user_input == "1":
        update_employee_menu()
        #Sends you to Update Employee
    elif user_input == "2":
        update_voyage()
        #Sends you to Update Voyage
    elif user_input == MAINMENU:
        first_menu()

    elif user_input == BACK:
        first_menu()
    else:
        print("Invalid input")
        upd_menu()

def update_employee_menu():
    ''' Updates a already existing data found in various CSV files '''
    ssn = input("Enter employee SSN: ")
    find_employee = Get_Data(2,ssn)
    employee_printer = find_employee.get_specific_emp()
    new_dict = {}
    #make list to a dict
    for item in employee_printer:
        name = item.pop('ssn')
        new_dict[name] = item

    if employee_printer == False:
            print("No employee with that SSN")
    elif ssn == CANCEL:
        first_menu()
        return
    else:
        print("##################################################")
        for row in employee_printer:
            for i in row:
                print("|  {:17}: {:26} | ".format(i,row[i]))
            print("##################################################")
        print()
        print()
    what_emp_update = input("What information to change: ")
   
    role = ""
    rank = ""
    licence = ""
    mobile = ""
    address = ""
    if what_emp_update == "role":
        role = input("Role: ")
        if role == CANCEL:
            first_menu()
            return
    else:
        role = item["role"]

    if what_emp_update == "rank":
        rank = input("Rank: ")
        if rank == CANCEL:
            first_menu()
            return
    else:
        rank = item["rank"]
    
    if what_emp_update == "licence":
        licence = input("Licence: ")
        if licence == CANCEL:
            first_menu()
            return
    else:
        licence = item["licence"]
    
    if what_emp_update == "address":
        address = input("Address: ")
        if address == CANCEL:
            first_menu()
            return
    else:
        address = item["address"]
    
    if what_emp_update == "mobile":
        mobile = input("mobile: ")
        if mobile == CANCEL:
            first_menu()
            return
    else:
        mobile = item["mobile"]
    
    firstname = item["firstname"]
    lastname = item["lastname"]

    new_emp = Employee(ssn, firstname, lastname, role, rank, licence, address, mobile)
    new_emp.update_employee()

    first_menu()

def Reg_menu():
    ''' Registers new Data and appends them to CSV files '''
    register_menu.build_title()
    register_menu.build_menu()
    print("")
    user_input = input("Choose an option: ")
    if user_input == "1":
        New_employee()
        #Create new employee
    elif user_input == "2":
        New_destination()
        #Create new destination
    elif user_input == "3":
        New_voyage()
        #Create new voyage
    elif user_input == "4":
        New_aircraft()
        #Create new aircraft   
    elif user_input == MAINMENU:
        first_menu()
        
    elif user_input == BACK:
        first_menu()
    else:
        print("Invalid input")
        Reg_menu()


def get_menu():
    ''' Reads a CSV file to list data '''
    listing_menu.build_title()
    listing_menu.build_menu()
    print("")
    user_input = input("Choose an option: ")
    if user_input == "1":
        emplist = Get_Data(2)
        #2 is constant for Crew
        empprinter = emplist.get_emp_list()
        print("")
        print("##################################################")
        for row in empprinter:
            for i in row:
                print("|  {:17}: {:26} | ".format(i,row[i]))
            print("##################################################")
        print()
        get_sub_menu()
        #List employees
    elif user_input == "2":
        get_menu_destinations()
        #List destinations
    elif user_input == "3":
        get_voyage()
        #List destinations
    elif user_input == "4":
        print("Not enough time.")
        first_menu()

    elif user_input == MAINMENU:
        first_menu()

    elif user_input == BACK:
        first_menu()
    else:
        print("Invalid input")
        get_menu()


def New_employee():
    ''' Creates a new employee '''
    register_emp_menu.build_title()
    register_emp_menu.build_menu()
    
    ssn = input("SSN: ")
    if ssn == CANCEL:
        first_menu()
        return
    
    firstname = input("First name: ")
    if firstname == CANCEL:
        first_menu()
        return
    
    lastname = input("Last name: ")
    if lastname == CANCEL:
        first_menu()
        return
    
    role = input("Role: ")
    if role == CANCEL:
        first_menu()
        return
    
    rank = input("Rank: ")
    if rank == CANCEL:
        first_menu()
        return
    
    licence = input("Licence: ")
    if licence == CANCEL:
        first_menu()
        return
    elif licence == "":
        licence = "N/A"
    
    address = input("Address: ")
    if address == CANCEL:
        first_menu()
        return
    
    mobile = input("Mobile: ")
    if mobile == CANCEL:
        return

    new_emp = Employee(ssn, firstname, lastname, role, rank, licence, address, mobile)
    new_emp.save_employee()
    
    Reg_menu()
    
def update_voyage():
    ''' Updates excisting data on voyages '''
    date_from_iceland = input("Enter date of voyage (YYYY-MM-DDThh:mm:ss): ")
    find_voyage = Get_Data(6,None,None,None,date_from_iceland)
    voyage_printer = find_voyage.get_voyage_day()
    new_dict = {}
    #Converting a list to a dict to handle the updates
    for item in voyage_printer:
        name = item.pop('date_from_iceland')
        new_dict[name] = item
    if voyage_printer == False:
            print("No flights listed on this date!")
    elif date_from_iceland == CANCEL:
        first_menu()
        return
    else:
        print("#############################################################")
        for row in voyage_printer:
            for i in row:
                print("|  {:28}: {:26} | ".format(i,row[i]))
            print("#############################################################")
        print()
        print()
    what_voy_update = input("What information to change: ")
   
    pilot_captain = ""
    pilot_copilot = ""
    flight_attendant_supervisor = ""
    flight_attendant = ""

    if what_voy_update == "pilot_captain":
        pilot_captain = input("Pilot captain: ")
        if pilot_captain == CANCEL:
            first_menu()
            return
    else:
        pilot_captain = item["pilot_captain"]

    if what_voy_update == "pilot_copilot":
        pilot_copilot = input("pilot_copilot: ")
        if pilot_copilot == CANCEL:
            first_menu()
            return
    else:
        pilot_copilot = item["pilot_copilot"]
    
    if what_voy_update == "flight_attendant_supervisor":
        flight_attendant_supervisor = input("Flight attendant supervisor: ")
        if flight_attendant_supervisor == CANCEL:
            first_menu()
            return
    else:
        flight_attendant_supervisor = item["flight_attendant_supervisor"]
    
    if what_voy_update == "flight_attendant":
        flight_attendant = input("Flight attendant: ")
        if flight_attendant == CANCEL:
            first_menu()
            return
    else:
        flight_attendant = item["flight_attendant"]
    
    destination = item["destination"]
    date_back_to_iceland = item["date_back_to_iceland"]

    new_voy = Voyage(date_from_iceland, destination, date_back_to_iceland, pilot_captain, pilot_copilot, flight_attendant_supervisor, flight_attendant)
    new_voy.update_voyage()

    first_menu()

def New_aircraft():
    ''' Creates a new aircraft '''
    aircraft_type = input("Aircraft type: ")
    num_seats = input("Number of seats: ")
    manufacturer = input("Manufacturer: ")
    name_of_aircraft = input("Name of aircraft: ")
    
    airc_str = Aircraft(aircraft_type, num_seats, manufacturer, name_of_aircraft)
    airc_str.store_aircraft()

    Reg_menu()

def New_destination():
    ''' Creates a new destination '''
    short = input("ID: ")
    if short == CANCEL:
        first_menu()
        return
    location = input("location: ")
    if location == CANCEL:
        first_menu()
        return
    airport = input("Airport: ")
    if airport == CANCEL:
        first_menu()
        return
    flighttime = input("Flighttime: ")
    if flighttime == CANCEL:
        first_menu()
        return
    distance = input("Distance: ")
    if distance == CANCEL:
        first_menu()
        return
    emergencycontact = input("Emergency contact: ")
    if emergencycontact == CANCEL:
        first_menu()
        return
    emergencynumber = input("Emergency number: ")
    if emergencynumber == CANCEL:
        first_menu()
        return

    
    dest_str = Destination(short, location, airport, flighttime, distance, emergencycontact, emergencynumber)
    dest_str.store_destination()

    Reg_menu()

def New_voyage():
    ''' Creates a new voyage '''
    flown_tday = True
    destination = input("Destination: ")
    if destination == CANCEL:
            first_menu()
            return

    date_from_iceland = input("Date From Iceland: ")
    if date_from_iceland == CANCEL:
            first_menu()
            return

    date_back_from_iceland = input("Date Back To Iceland: ")
    if date_back_from_iceland == CANCEL:
            first_menu()
            return

    while flown_tday:
        pilot_captain = input("Captain: ")
        if pilot_captain == CANCEL:
            first_menu()
            return
        checker = Get_Data(6,None,None,pilot_captain,date_from_iceland,1)
        #Checks if the pilot has already flown today
        flown_tday = checker.get_checker()
        if flown_tday == True:
            print("Employee has already flown today. Choose another.")
    flown_tday = True
    while flown_tday:
        pilot_copilot = input("CoPilot: ")
        if pilot_copilot == CANCEL:
            first_menu()
            return
        checker = Get_Data(6,None,None,pilot_copilot,date_from_iceland,2)
        #Checks if the pilot has already flown today
        flown_tday = checker.get_checker()
        if flown_tday == True:
            print("Employee has already flown today. Choose another.")
    flown_tday = True
    while flown_tday:
        flight_attendant_supervisor = input("Flight Attendant Supervisor: ")
        if flight_attendant_supervisor == CANCEL:
            first_menu()
            return
        checker = Get_Data(6,None,None,flight_attendant_supervisor,date_from_iceland,3)
        #Checks if the flight attendant has already flown today
        flown_tday = checker.get_checker()
        if flown_tday == True:
            print("Employee has already flown today. Choose another.")
    flown_tday = True
    while flown_tday:
        flight_attendant = input("Flight Attendant: ")
        if flight_attendant == CANCEL:
            first_menu()
            return
        checker = Get_Data(6,None,None,flight_attendant,date_from_iceland,4)
        #Checks if the flight attendant has already flown today
        flown_tday = checker.get_checker()
        if flown_tday == True:
            print("Employee has already flown today. Choose another.")

    new_voy = Voyage(date_from_iceland, destination, date_back_from_iceland, pilot_captain, pilot_copilot, flight_attendant_supervisor, flight_attendant)
    new_voy.store_voyage()
      
    Reg_menu()


def get_sub_menu():
    ''' Selects how to list the employees '''
    print("")
    print("1. Find employee")
    print("2. Show pilots")
    print("3. Show flight attendants")
    print("4. Show employees on shift")
    print("5. Show employees not on shift")
    print("6. Find pilots with certain licence")
    print("7. Find a work week for a certain employee")
    print("")
    print('   [B]ack       [M]ain_menu')
    user_input_sec = input("Choose an option: ")
    print("")
    if user_input_sec == "1":
        #Finds a employee with a certain social security number
        ssn_temp = input("Enter SSN: ")
        print("")
        emp_spec = Get_Data(2, ssn_temp)
        emp_spec_printer = emp_spec.get_specific_emp()
        if emp_spec_printer == False:
            print("No employee with that SSN")
        else:
            print("##################################################")
            for row in emp_spec_printer:
                for i in row:
                    print("|  {:17}: {:26} | ".format(i,row[i]))
                print("##################################################")
            print()
        print()
        input("Press ENTER to continue.. ")
        get_sub_menu()
    
    elif user_input_sec == "2":
        #Lists pilots
        emp_pilots = Get_Data(2)
        emp_pilots_printer = emp_pilots.get_pilots()
        print("##################################################")
        for row in emp_pilots_printer:
            for i in row:
                print("|  {:17}: {:26} | ".format(i,row[i]))
            print("##################################################")
        print()
        input("Press ENTER to continue.. ")
        get_sub_menu()

    elif user_input_sec == "3":
        #Lists flight attendants
        emp_cabin = Get_Data(2)
        emp_cabin_printer = emp_cabin.get_flightattendants()
        print("##################################################")
        for row in emp_cabin_printer:
            for i in row:
                print("|  {:17}: {:26} | ".format(i,row[i]))
            print("##################################################")
        print()
        input("Press ENTER to continue.. ")
        get_sub_menu()

    elif user_input_sec == "4":
        #Lists who are currently working
        emp_working = Get_Data(2)
        emp_working_printer = emp_working.get_emp_working()
        print("##################################################")
        for row in emp_working_printer:
            for i in row:
                print("|  {:17}: {:26} | ".format(i,row[i]))
            print("##################################################")
        print()
        input("Press ENTER to continue.. ")
        get_sub_menu()

    elif user_input_sec == "5":
        #List who are currently not working
        emp_notworking = Get_Data(2)
        emp_notworking_printer = emp_notworking.get_emp_not_working()
        print("##################################################")
        for row in emp_notworking_printer:
            for i in row:
                print("|  {:17}: {:26} | ".format(i,row[i]))
            print("##################################################")
        print()
        input("Press ENTER to continue.. ")
        get_sub_menu()

    elif user_input_sec == "6":
        #Lists pilots with that type of licence
        licence_temp = input("Enter aircraft type: ")
        print("")
        pilots_licence = Get_Data(2,None,licence_temp)
        pilots_licence_printer = pilots_licence.get_pilots_from_airtype()
        if pilots_licence_printer == False:
            print("No pilot with that perticular licence")
        else:
            print("##################################################")
            for row in pilots_licence_printer:
                for i in row:
                    print("|  {:17}: {:26} | ".format(i,row[i]))
                print("##################################################")
        print()
        input("Press ENTER to continue.. ")
        get_sub_menu()

    elif user_input_sec == "7":
        #Lists all voyages flown by a certain employee by week
        name_of_temp = input("Enter name of employee: ")
        date_temp = input("Enter a date: ")
        print("")
        date_checker = Get_Data(6,None,None,name_of_temp,date_temp)
        date_checker_printer = date_checker.get_voyage_emp_week()
        if date_checker_printer == False:
            print("No flights listed in this ")
        else:
            print("#############################################################")
            for row in date_checker_printer:
                for i in row:
                    print("|  {:28}: {:26} | ".format(i,row[i]))
                print("#############################################################")
        print()
        input("Press ENTER to continue.. ")
        get_sub_menu()

    elif user_input_sec == MAINMENU:
        first_menu()
    elif user_input_sec == BACK:
        get_menu()

    elif user_input_sec == MAINMENU:
        first_menu()
    elif user_input_sec == BACK:
        get_menu()

def get_menu_destinations():
    ''' Lists destinations '''
    destinations = Get_Data(3)
    destinations_printer = destinations.get_destinations()
    print("##################################################")
    for row in destinations_printer:
        for i in row:
            print("|  {:17}: {:26} | ".format(i,row[i]))
        print("##################################################")
    print()
    input("Press ENTER to continue.. ")
    get_menu()

def get_voyage():
    ''' Lists voyages '''
    voyage = Get_Data(6)
    voyage_printer = voyage.get_voyage()
    print("#############################################################")
    for row in voyage_printer:
        for i in row:
            print("|  {:28}: {:26} | ".format(i,row[i]))
        print("#############################################################")
    print("")
    print("1. Get voyages in a certain week")
    print("2. Get voyages by day")
    print("")
    print('   [B]ack       [M]ain_menu')
    user_input_sec = input("Choose an option: ")
    print("")
    if user_input_sec == "1":
        #Get voyages in a certain week
        date_temp = input("Enter a date: ")
        print("")
        date_checker = Get_Data(6,None,None,None,date_temp)
        date_checker_printer = date_checker.get_voyage_week()
        if date_checker_printer == False:
            print("Enginn flug í þessari viku")
        else:
            print("#############################################################")
            for row in date_checker_printer:
                for i in row:
                    print("|  {:28}: {:26} | ".format(i,row[i]))
                print("#############################################################")
        print()
        input("Press ENTER to continue.. ")
        get_voyage()

    elif user_input_sec == "2":
        #Get voyages by day
        date_temp = input("Enter a date: ")
        print("")
        date_checker = Get_Data(6,None,None,None,date_temp)
        date_checker_printer = date_checker.get_voyage_day()
        if date_checker_printer == False:
            print("Enginn flug í þessari viku")
        else:
            print("#############################################################")
            for row in date_checker_printer:
                for i in row:
                    print("|  {:28}: {:26} | ".format(i,row[i]))
                print("#############################################################")
        print()
        input("Press ENTER to continue.. ")
        get_voyage()

    elif user_input_sec == MAINMENU:
        first_menu()

    elif user_input_sec == BACK:
        get_menu()

first_menu()