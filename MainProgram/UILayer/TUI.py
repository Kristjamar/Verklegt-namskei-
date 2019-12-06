from prufa.datalayer.datalayertest import Database

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
        Reg_emp()
        
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
    
first_menu()