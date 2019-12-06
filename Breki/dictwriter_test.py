import csv

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
    def new_employee(self):



    def make_employee(self):
        with open('employeetest.csv', 'a', newline='') as csvfile:
            fieldnames = ['first_name', 'last_name','SSN','title','phone_number','mobile','email','address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'first_name': self.first, 'last_name': self.last, 'SSN': self.socialnumber,'title': self.title ,'phone_number': self.phonenumber,'mobile': self.mobile,'email': self.email_str,'address': self.address})

class Menu:
    def __init__(self, title, option1, option2, option3, option4, option5, option6, option7, option8, option9, how_many_options):
        self.title = title
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.option5 = option5
        self.option6 = option6
        self.option7 = option7
        self.option8 = option8
        self.option9 = option9
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
        elif self.how_many_options == 5:
            print("5.{}".format(self.option5))
        elif self.how_many_options == 6:
            print("6.{}".format(self.option6))
        elif self.how_many_options == 7:
            print("7.{}".format(self.option7))
        elif self.how_many_options == 8:
            print("8.{}".format(self.option8))
        elif self.how_many_options == 9:
            print("9.{}".format(self.option9))
        
        print()
        print('[B]ack       [M]ain_menu')
        return ""
Register_sub = Menu("Nýskrá", "Fyrirnafn:", "Eftirnafn:", "Kennitala:","Titill","Símanúmer","Gemsasúmer:","Netfang:","Heimilisfang:" "3")
# emp_1 = Employee("Breki", "Hardarson", "1206963359","Meistari", "5812345", "7891234", "Heimahjamer 2",)
# emp_2 = Employee("Haffi", "Stfnsn", "4204206969","Co-Meistari", "4217575", "8773821", "Heimahonum 1",)
employee_dict = {}
def add_to_dict(employee_dict):
    key = input("Key: ")
    value = input("Value: ")
    if key in x:
        print("Error. Key already exists.")
        return x
    else:
        x[key] = value
        return x
 
def fknskitashit():
    emp_firstname_input = input("First name: ")
    if emp_firstname_input = type(int):
        print("Please enter a valid name")
    else:
        temp_emp{} += empfirstname,","
    emp_lastname_input = input("Last name: ")
    if emp_lastname_input = type(int):
        print("Please enter a valid name")
    else:
        temp_emp += emp_lastname_input,","
    emp_ssn_input = input("SSN: ")
    if emp_ssn_input = type(str):
        print("Please enter a valid SSN")
    else:
        temp_emp += emp_ssn_input

    emp_title_input = input("Title: ")
    if emp_title_input = type(int):
        print("Please enter a valid title")
    else:
        temp_emp += emp_n,","

    emp_mobile_input = input("Mobile: ")
    if emp_mobile_input = type(str):
        print("Please enter a valid mobile number")
    else:
        temp_emp += emp_mobile_input,","

    emp_email = emp_firstname_input + emp_lastname_input

    emp_address_input = input("Address: ")
    if emp_mobile_input = type(str):
        print("Please enter a valid mobile number")
    else:
        temp_emp += emp_mobile_input,","






def new_employee()
emp_1.make_employee()
emp_2.make_employee()