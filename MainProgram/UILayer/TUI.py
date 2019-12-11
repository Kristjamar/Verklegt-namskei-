from LogicLayer.logiclayer import Employee , Aircraft, Get_Data, Destination

MAINMENU = "m" or "M"
BACK = "b" or "B"
QUIT = "q" or "Q"


class Menu:
    def __init__(self, title, option1, option2, option3, option4, option5, option6, option7, how_many_options):
        self.title = title
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.option5 = option5
        self.option6 = option6
        self.option7 = option7
        self.how_many_options = how_many_options

    def build_menu(self):
        print("########################################")
        print("##{:^36}##".format(self.title))
        print("########################################")
        print("#                                      #")
        print("# 1.{:34} #".format(self.option1))
        print("# 2.{:34} #".format(self.option2))
        print("# 3.{:34} #".format(self.option3))
        if self.how_many_options >= 4:
            print("# 4.{:34} #".format(self.option4))
        if self.how_many_options >= 5:
            print("# 5.{:34} #".format(self.option5))
        if self.how_many_options >= 6:
            print("# 6.{:34} #".format(self.option6))
        if self.how_many_options == 7:
            print("# 7.{:34} #".format(self.option7))
        print("#                                      #")
        print("########################################")
        if self.title == "Main Menu":
            print("[Q]uit")
        elif self.how_many_options <=4:
            print('[B]ack       [M]ain_menu')
        
        
        return ""
        '''Makes building a menu easier'''

        
    # def title(self):
    #     print("#############################")
    #     print("------{}------".format(self.title))
    #     print("#############################")
    #     print()
    #     return ""

main_menu = Menu("Main Menu", "Búa til", "Upplýsingar", "Uppfæra","","","","", 3)
register_menu = Menu("Nýskrá", "Skrá starfsmann", "Skrá áfangastað", "Skrá vinnuferð", "Skrá flugvél","","","", 4)
listing_menu = Menu("Upplýsingar", "Birta starfsmenn", "Birta áfangastaði", "Birta vinnuferðir", "Birta tegund flugvéla","","","", 4)
update_menu = Menu("Uppfæra", "Uppfæra starfsmenn", "Uppfæra áfangastaði", "Uppfæra vinnuferðir", "Uppfæra flugvél","","","", 4)
register_emp_menu = Menu("Skrá starfsmann", "Fyrirnafn:(Jón)", "Eftirnafn:(Jónsson)", "Titill:(Flugstjóri)", "Heimanúmer:(4335858)","Farsími:(5812345)","Netfang:(Jonjonsson@nan.is)","Heimilisfang:(Bankastræti 5)", 7)

def first_menu():
    main_menu.build_menu()
    print("")
    user_input = input("Veldu valmöguleika: ")
    
    if user_input == "1":
        Reg_menu()
    elif user_input == "2":
        get_menu()
    elif user_input == "3":
        update_menu.build_menu()
        get_menu()
    elif user_input == QUIT:
        exit
    else:
        print("Invalid input")

def Reg_menu():
    print(register_menu.build_menu())
    print("")
    user_input = input("Veldu valmöguleika: ")
    if user_input == "1":
        emp_str = New_employee()
        firstname, lastname, ssn, title , phonenumber, mobile, address = emp_str
        emp_1 = Employee(firstname, lastname, ssn, title , phonenumber, mobile, address)
        emp_1.save_employee()
        
    elif user_input == "2":
        dest_str = New_destination()
        country, city, airport, flighttime, distance, emergencycontact, emergencynumber = dest_str
        dest_1 = Destination(country, city, airport, flighttime, distance, emergencycontact, emergencynumber)
        dest_1.save_destination()

    elif user_input == "3":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()

    elif user_input == "4":
        airc_str = New_aircraft()
        aircraft_type, num_seats, manufacturer, name_of_aircraft = airc_str
        airc_1 = Aircraft(aircraft_type, num_seats, manufacturer, name_of_aircraft)
        airc_1.save_aircraft()
    
    elif user_input == MAINMENU:
        first_menu()
    elif user_input == BACK:
        first_menu()

def get_menu():
    print(listing_menu.build_menu())
    print("")
    user_input = input("Veldu valmöguleika: ")
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

    elif user_input == "2":
        get_menu_destinations()
    elif user_input == "3":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()
    elif user_input == "4":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()

    elif user_input == MAINMENU:
        first_menu()
    elif user_input == BACK:
        first_menu())


def New_employee():
    
    register_emp_menu.build_menu()
    firstname = input("Fyrirnafn: ")
    lastname = input("Eftirnafn: ")
    ssn = input("Kennitala: ")
    title = input("Titill: ")
    phonenumber = int(input("Heimasími: "))
    mobile = int(input("Farsími: "))
    address = input("Heimilisfang: ")
    emp_str = firstname, lastname, ssn, title , phonenumber, mobile, address
    #return firstname, lastname, ssn, title , phonenumber, mobile, address
    return emp_str
    

def New_aircraft():
        aircraft_type = input("aircraft_type: ")
        num_seats = input("num_seats: ")
        manufacturer = input("manufacturer: ")
        name_of_aircraft = input("name_of_aircraft: ")
        
        airc_str = aircraft_type, num_seats, manufacturer, name_of_aircraft
        #return aircraft_type, num_seats, manufacturer, name_of_aircraft
        return airc_str

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


def get_sub_menu():
    print("")
    print("1. Finna starfsmann")
    print("2. Birta flugmenn")
    print("3. Birta flugþjóna")
    print("4. Birta starfsmenn á vakt")
    print("5. Birta starfsmenn ekki á vakt")
    print("6. Finna flugmenn eftir flugvélategund")
    print("")
    print('   [B]ack       [M]ain_menu')
    user_input_sec = input("Veldu valmöguleika: ")
    print("")
    if user_input_sec == "1":
        ssn_temp = input("Sladu inn kennitolu: ")
        print("")
        emp_spec = Get_Data(2, ssn_temp)
        emp_spec_printer = emp_spec.get_specific_emp()
        if emp_spec_printer == False:
            print("Enginn starfsmaður með þessa kennitölu")
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
        licence_temp = input("Sladu inn flugvelategund: ")
        print("")
        pilots_licence = Get_Data(2,None,licence_temp)
        pilots_licence_printer = pilots_licence.get_pilots_from_airtype()
        if pilots_licence_printer == False:
            print("Enginn flugmaður með leyfi á þessa tilteknu vél")
        else:
            print("##################################################")
            for row in pilots_licence_printer:
                for i in row:
                    print("|  {:17}: {:26} | ".format(i,row[i]))
                print("##################################################")
        print()
        input("Press ENTER to continue.. ")
        get_sub_menu()

    elif user_input_sec == MAINMENU:
        first_menu()
    elif user_input_sec == BACK:
        get_menu()

def get_menu_destinations():
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
    voyage = Get_Data(6)
    voyage_printer = voyage.get_voyage()
    print("##################################################")
    for row in voyage_printer:
        for i in row:
            print("|  {:17}: {:26} | ".format(i,row[i]))
        print("##################################################")
    print()
    input("Press ENTER to continue.. ")
    get_menu()

first_menu()
#Make employee from user input
#Send that information to the Employee class
#Send the employee to csv from there
#so Save_employee should be in the Employee class and take in all the information and make another dict for some reason