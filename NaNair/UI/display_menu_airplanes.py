from UI.airplaneUI import AirplaneUI
from UI.display_menu_airplane_type import DisplayMenuAirplaneType

class DisplayMenuAirplanes: 
    def __init__(self, logic_layer):
        print('Display airplanes')

    def startDisplayAirplanes(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Airplanes'))
        print('#'*20)
        print()

        while True: 
            print('What would you like to display?')
            print()
            print('1 - List all airplanes')
            print('2 - List airplanes by type')
            print('m - Go back to display menu')
            print()

            selection = input()

            if selection == '1':
                '''Gets all airplanes'''
                AirplaneUI().showAllPlanes()

            elif selection == '2':
                '''Gets all airplanes by type'''
                DisplayMenuAirplaneType().startDisplayAirplaneType()

            elif selection == 'm':
                '''Goes back to main menu'''
                return
            else: 
                print('Invalid selection')