class SubMenuEdit:
    def __init__(self):
        print('sub menu Edit')

    def startSubMenuEdit(self):
        print('EDIT EXISTING DATA')
        print('What would you like to edit? ')

        start = True
        
        while start: 
            print('1 - Existing voyage')
            print('2 - Destination')
            print('m - Main menu')

            selection = input()

            if selection == '1': 
                start = False
            elif selection == '2':
                start = False
            elif selection == 'm':
                #next_menu = MainMenu()
                start = False
            else:
                print("Invalid selection")