from UI.crewUI import CrewUI
from API.LL_API import LL_API
from ModelClasses.flight_att_model import FlightAttendant
from ModelClasses.pilot_model import Pilot
from UI.EditMenus.edit_employee_licence import EditEmployeeLicense


class EditEmployeeMenu:
    def printEditEmployeeMenu(self,crew_id, employee):
        '''Editing menu for a single crew member'''

        print('What would you like to change?')
        print()
        print('1 - Address')
        print('2 - Phone number')
        print('3 - Email')
        print('4 - Rank')

        # flight attendants do not have a license
        if type(employee) == Pilot:
            print('5 - License')

        print('m - Back to main menu')
        print()

    def editSelection(self,crew_id):
        '''Redirects to UI methods based on user selection'''
        
        # employee instance found from crew id
        employee = LL_API().get_crew_member_by_id(crew_id)
        
        self.printEditEmployeeMenu(crew_id,employee)
        
        
        selection = input('Please choose one of the above: ').strip()
        if selection == '1':
            ''' The software asks for new home adress and assigns it to the owner of given ID'''
            new_address = CrewUI().getHomeAddress()
            employee.setAddress(new_address)
            return CrewUI().changeEmployeeInfo(employee)

        elif selection == '2':
            ''' The software asks for new phone number and assigns it to the owner of given ID'''
            new_phonenumber = CrewUI().getPhoneNumber()
            employee.setPhonenumber(new_phonenumber)
            return CrewUI().changeEmployeeInfo(employee)

        elif selection == '3':
            ''' The software asks for new email adress and assigns it to the owner of given ID'''
            new_email_address = CrewUI().getEmail()
            employee.setEmail(new_email_address)
            return CrewUI().changeEmployeeInfo(employee)

        elif selection == '4':
            ''' The software asks for new rank and assigns it to the owner of given ID'''
            while True:
                if type(employee) == Pilot:
                    print()
                    print('Please choose one: ')
                    print('0 - Co-pilot')
                    print('1 - Captain')
                    print('m - Back to main menu')
                else: 
                    print()
                    print('Please choose one: ')
                    print('0 - Flight attendant')
                    print('1 - Head service manager')
                    print('m - Back to main menu')
                print()
                new_rank = input('Please choose one of the above: ').strip()

                if new_rank != '0' and new_rank != '1' and new_rank != 'm':
                    print('\nInvalid rank!\n')

                elif new_rank == 'm':
                    return

                else:
                    employee.setRank(new_rank)
                    CrewUI().changeEmployeeInfo(employee)
                    return
            
        elif selection == '5':
            ''' The software asks for new license and assigns it to the owner of given ID'''
            return EditEmployeeLicense().startEditEmployeeLicense(employee)

        elif selection == 'm':
            '''user is redirected to main menu'''
            return

        else:
            print("\nInvalid input!\n")