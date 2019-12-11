from logiclayer.logiclayertest import Get_Data

class Menu:
    def __init__(self, title, option1, option2, option3, option4, how_many_options):
        self.title = title
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.how_many_options = how_many_options

    def build_menu(self):
        print("##############################")
        print("##{:^26}##".format(self.title))
        print("##############################")
        print("#                            #")
        print("# 1.{:24} #".format(self.option1))
        print("# 2.{:24} #".format(self.option2))
        print("# 3.{:24} #".format(self.option3))

        if self.how_many_options == 4:
            print("# 4.{:24} #".format(self.option4))

        print("#                            #")
        print("##############################")
        print('[B]ack       [M]ain_menu')

        return ""

    def mainmenu(self):
        print("##############################")
        print("##{:^26}##".format(self.title))
        print("##############################")
        print("#                            #")
        print("# 1.{:24} #".format(self.option1))
        print("# 2.{:24} #".format(self.option2))
        print("# 3.{:24} #".format(self.option3))
        print("#                            #")
        print("##############################")
        print("[Q]uit")

        return ""


def menu_builder():
    MAINMENU = "m" or "M"
    BACK = "b" or "B"
    QUIT = "q" or "Q"

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
            prufa = Get_Data(2)
            prufa.get_emp_list()
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

    def get_menu():
        user_input = input("Veldu valmöguleika: ")
        if user_input == "1":
            emplist = Get_Data(2)
            empprinter = emplist.get_emp_list()
            [print(row) for row in empprinter]
            print("")
            print("1. Finna starfsmann")
            print("2. Leita eftir dagsetningu")
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
                    print(emp_spec_printer)
            elif user_input_sec == "2":
                pass
            elif user_input_sec == MAINMENU:
                first_menu()
            elif user_input_sec == BACK:
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
        
    # def get_emp_menu():



    #     elif user_input == MAINMENU:
    #         first_menu()
    #     elif user_input == BACK:
    #         first_menu()

    first_menu()