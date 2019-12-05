from UI.crewUI import CrewUI


class EditEmployeeMenu:
    def __init__(self):
        pass

    def printEditEmployeeMenu(self,employee):
        print('What would you like to change?')
        print()
        try:
            employee.getCaptain()
            print('1 - Address')
            print('2 - Phone number')
            print('3 - Email')
            print('4 - Rank')
            print('5 - License')
            print()
        except AttributeError:
            print('1 - Address')
            print('2 - Phone number')
            print('3 - Email')
            print('4 - Rank')
            print()

    def editSelection(self,employee):
        EditEmployeeMenu().printEditEmployeeMenu(employee)
        selection = input()
        if selection == '1':
            new_address = input("New address: ")
            CrewUI().changeEmployeeAddress(employee, new_address)

        elif selection == '2':
            new_phonenumber = input('New Phone number: ')

        elif selection == '3':
            new_email_address = input('New email: ')
            CrewUI().changeEmployeeEmail(employee, new_email_address)

        elif selection == '4':
            new_rank = input('Rank: ')

        elif selection == '5':
            new_license = input('License: ')

        else:
            print("Invalid input")  