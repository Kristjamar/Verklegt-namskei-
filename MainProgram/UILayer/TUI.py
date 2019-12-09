from LogicLayer.logiclayer import Employee

MAINMENU = "m" or "M"
BACK = "b" or "B"
QUIT = "q" or "Q"


class Menu:
    def __init__(self, title, option1, option2, option3, option4, how_many_options):
        self.title = title
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.how_many_options = how_many_options

    def build_menu(self):
        print("#############################")
        print("------{}------".format(self.title))
        print("#############################")
        print()
        print("1.{}".format(self.option1))
        print("2.{}".format(self.option2))
        print("3.{}".format(self.option3))
        if self.how_many_options == 4:
            print("4.{}".format(self.option4))
        print()
        print('[B]ack       [M]ain_menu')
        return ""
    def mainmenu(self):
        print("#############################")
        print("------{}------".format(self.title))
        print("#############################")
        print()
        print("1.{}".format(self.option1))
        print("2.{}".format(self.option2))
        print("3.{}".format(self.option3))
        print()
        print("[Q]uit")
        return ""

main_menu = Menu("Main Menu", "Búa til", "Upplýsingar", "Uppfæra","", "3")
register_menu = Menu("Nýskrá", "Skrá starfsmann", "Skrá áfangastað", "Skrá vinnuferð", "Skrá flugvél", 4)
listing_menu = Menu("Upplýsingar", "Birta starfsmenn", "Birta áfangastaði", "Birta vinnuferðir", "Birta tegund flugvéla", 4)
update_menu = Menu("Uppfæra", "Uppfæra starfsmenn", "Uppfæra áfangastaði", "Uppfæra vinnuferðir", "Uppfæra flugvél", 4)

def first_menu():
    print(main_menu.mainmenu())
    user_input = input("Veldu valmöguleika: ")
    if user_input == "1":
        Reg_menu()
    elif user_input == "2":
        print(listing_menu.build_menu())
        tmp_menu()
    elif user_input == "3":
        print(update_menu.build_menu())
        tmp_menu()
    elif user_input == QUIT:
        exit
    else:
        print("Invalid input")

def Reg_menu():
    print(register_menu.build_menu())
    user_input = input("Veldu valmöguleika: ")
    if user_input == "1":
        emp_str = New_employee()
        firstname, lastname, ssn, title , phonenumber, mobile, address = emp_str
        emp_1 = Employee(firstname, lastname, ssn, title , phonenumber, mobile, address)
        emp_1.save_employee()
        
    elif user_input == "2":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()
    elif user_input == "3":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()
    elif user_input == "4":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()
    elif user_input == MAINMENU:
        first_menu()
    elif user_input == BACK:
        first_menu()

def tmp_menu():
    user_input = input("Veldu valmöguleika: ")
    if user_input == "1":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()
    elif user_input == "2":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()
    elif user_input == "3":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()
    elif user_input == "4":
        print("WIP MENU, sendi þig aftur á Main menu")
        first_menu()

    elif user_input == MAINMENU:
        first_menu()
    elif user_input == BACK:
        first_menu()


def New_employee():
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
    
def save_employee(emp_dict):
            with open('employeetest.csv', 'a', newline='') as csvfile:
                    fieldnames = ['first_name', 'last_name','SSN','title','phone_number','mobile','email','address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    writer.writerow(emp_dict)

first_menu()

#Make employee from user input
#Send that information to the Employee class
#Send the employee to csv from there
#so Save_employee should be in the Employee class and take in all the information and make another dict for some reason