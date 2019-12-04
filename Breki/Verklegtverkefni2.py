#Setja saman main menu
#Three options
#Nýtt, Skoða og uppfæra

def menu(name,option1,option2,option3):
    print("#############################")
    print("------{}------".format(name))
    print("#############################")
    print()
    print("1.{}".format(option1))
    print("2.{}".format(option2))
    print("3.{}".format(option3))
    print()
    print('B\u0332ack       C\u0332ancel')

def main():
    name = input("Enter what you want the menu to be called: ")
    option1 = input("Enter what the first option should be: ")
    option2 = input("Enter what the second option should be: ")
    option3 = input("enter what the third option should be: ")
    menu(name,option1,option2,option3)
main()
