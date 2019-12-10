import csv

class Employee:
    __firstname=""
    __lastname=""
    __ssn= 0
    __title=""
    __phonenum=0
    __mobilenum=0
    __email=""
    __address=""
    def showData(self):
        print("Firstname:\t",self.__firstname) 
        print("Lastname:\t", self.__lastname)
        print("Ssn:\t\t", self.__ssn)
        print("Title:\t\t", self.__title)
        print("Phonenum:\t", self.__phonenum)
        print("Mobile_number:\t", self.__mobilenum)
        print("Email:\t\t", self.__email)
        print("Address:\t", self.__address)

    def setData(self):
        self.__firstname=input("Enter firstname:")
        Employee.showData(self)
        self.__lastname = input("Enter lastname:")
        Employee.showData(self)
        self.__ssn = int(input("Enter ssn:"))
        Employee.showData(self)
        self.__title = input("Enter title:")
        Employee.showData(self)
        self.__phonenum = int(input("Enter phone number:"))
        Employee.showData(self)
        self.__mobilenum = int(input("Enter mobile number:"))
        Employee.showData(self)
        self.__email = input("Enter email:")
        Employee.showData(self)
        self.__address = input("Enter address:")
        Employee.showData(self)
    def dict_employee(self):
        employee_ready = {'first_name': self.__firstname, 'last_name': self.__lastname, 'SSN': self.__ssn,'title': self.__title ,'phone_number': self.__phonenum,'mobile': self.__mobilenum,'email': self.__email,'address': self.__address}
        return employee_ready

    def save_employee(self):
        with open('employeetest.csv', 'a', newline='') as csvfile:
                fieldnames = ['first_name', 'last_name','SSN','title','phone_number','mobile','email','address']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow(Employee.dict_employee(self))


def Reg_emp():
    #Employee Object
    emp=Employee()
    emp.showData()
    emp.setData()
    emp.save_employee()

# class Employee():
#     def __init__(self, firstlastname, lastlastname, socialnumber, title = "", phonenumber = 0 ,mobile = 0 ,address = ""):
#         self.first = firstlastname
#         self.last = lastlastname
#         self.title = title
#         self.socialnumber = socialnumber
#         self.phonenumber = phonenumber
#         self.mobile = mobile
#         self.email_str = firstlastname + lastlastname + "@nan.is"
#         self.address = address
#     def new_employee(self):



#     def make_employee(self):
#         with open('employeetest.csv', 'a', newline='') as csvfile:
#             fieldlastnames = ['first_lastname', 'last_lastname','SSN','title','phone_number','mobile','email','address']
#             writer = csv.DictWriter(csvfile, fieldlastnames=fieldlastnames)

#             writer.writerow({'first_lastname': self.first, 'last_lastname': self.last, 'SSN': self.socialnumber,'title': self.title ,'phone_number': self.phonenumber,'mobile': self.mobile,'email': self.email_str,'address': self.address})