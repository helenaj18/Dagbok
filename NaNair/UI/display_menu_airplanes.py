from UI.airplaneUI import AirplaneUI
from UI.display_menu_airplane_type import DisplayMenuAirplaneType
import datetime
from API.LL_API import LL_API

class DisplayMenuAirplanes: 

    def startDisplayAirplanes(self):
        print('-'*20)
        print('{:^20}'.format('DISPLAY - Airplanes'))
        print('-'*20)
        print()

        while True: 
            print('What would you like to display?')
            print()
            print('1 - List all airplanes')
            print('2 - List airplanes by type')
            print('3 - List airplanes by date and time')
            print('m - Back to main menu')
            print()

            selection = input().strip()

            #Prints all airplanes owned by NaN Air
            if selection == '1':
                return AirplaneUI().showAllPlanes()

            # Prints all airplanes that are a certain type, type is chosen on next screen
            elif selection == '2':
                return DisplayMenuAirplaneType().startDisplayAirplaneType()
            
            # Gets availability status on airplanes at an inputted date
            elif selection == '3':
                print('Enter the date you want to display')
                year_str = input('Year: ')
                month_str = input('Month: ')
                day_str = input('Day: ')
                hour_str = input('Hour: ')
                minute_str = input('Minute: ')

                # check if date input is valid
                year_int,month_int,day_int = LL_API().verifyDate(year_str,month_str,day_str)

                # checks if time input is valid
                hour_int,minute_int = LL_API().verifyTime(hour_str,minute_str)

                # get datetime object of inputted time
                datetime_object = datetime.datetime(year_int,month_int,day_int,hour_int,minute_int)

                return AirplaneUI().showAirplanesByDateTime(datetime_object)

            #Goes back to main menu
            elif selection == 'm':
                return
            # If none of the possibilities are chosen
            else: 
                print('Invalid selection!')
                print()