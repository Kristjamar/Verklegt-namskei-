#Setja saman main menu
#Three options
#Nýtt, Skoða og uppfæra

#class menu:
#    def __init__(self,title,)


MAINMENU = "m" or "M"
BACK = "b" or "B"
QUIT = "q" or "Q"


def menu(name,option1,option2,option3,option4,option5,how_many_options):
    print("#############################")
    print("------{}------".format(name))
    print("#############################")
    print()
    #for i in range(1,how_many_options+1):
    #    print(i,".","{}".format(""))
    
    print("1.{}".format(option1))
    print("2.{}".format(option2))
    print("3.{}".format(option3))
    if how_many_options == 4:
        print("4.{}".format(option4))
    elif how_many_options == 5:
        print("5.{}".format(option5))
    print()
    print('[B]ack       [M]ain_menu')

# def main_menu():
#     print("#############################")
#     print("------Main Menu------")
#     print("#############################")
#     print()
    
#     print("1.Búa til")
#     print("2.Birta")
#     print("3.Uppfæra")
    

def make_register_menu():
    how_many_options = 4
    name = "Nýskrá"
    option1 = "Skrá starfsmann"
    option2 = "Skrá áfangastað"
    option3 = "Skrá vinnuferð"
    option4 = "Skrá flugvél"
    option5 = ""
    
    menu(name,option1,option2,option3,option4,option5,how_many_options)

def tmp_menu():
    user_input = input("Veldu valmöguleika: ")

    if user_input == "1":
        print("WIP MENU")
    elif user_input == "2":
        print("WIP MENU")
    elif user_input == "3":
        print("WIP MENU")
    elif user_input == "4":
        print("WIP MENU")


    elif user_input == MAINMENU:
        first_menu()
    elif user_input == BACK:
        first_menu()

def make_main_menu():
    print("#############################")
    print("------Main Menu------")
    print("#############################")
    print()
    
    print("1.Búa til")
    print("2.Birta")
    print("3.Uppfæra")
    print()
    print("[Q]uit")

def make_listing_menu():
    how_many_options = 4
    name = "Upplýsingar"
    option1 = "Birta starfsmenn"
    option2 = "Birta áfangastaði"
    option3 = "Birta vinnuferðir"
    option4 = "Birta tegund flugvéla"
    option5 = ""
    
    menu(name,option1,option2,option3,option4,option5,how_many_options)

def make_update_menu():
    how_many_options = 4
    name = "Uppfærsla"
    option1 = "Uppfæra starfsmenn"
    option2 = "Uppfæra áfangastaði"
    option3 = "Uppfæra vinnuferðir"
    option4 = "Uppfæra flugvél"
    option5 = ""
    
    menu(name,option1,option2,option3,option4,option5,how_many_options)




def first_menu():
    make_main_menu()
    user_input = input("Veldu valmöguleika: ")
    
    if user_input == "1":
        make_register_menu()
        tmp_menu()
    elif user_input == "2":
        make_listing_menu()
        tmp_menu()
    elif user_input == "3":
        make_update_menu()
        tmp_menu()
    elif user_input == QUIT:
        exit

        
        
        
    else:
        print("Invalid input!")
        
        
        

#def second_menu():



first_menu()

#else:
#    quit