from UI.crewUI import CrewUI

class DisplayMenuPilots: 
    def __init__(self, logic_layer):
        print('Display pilots')

    def startDisplayPilots(self):
        print('#'*20)
        print('{:^20}'.format('DISPLAY - Pilots'))
        print('#'*20)
        print()

        start = True
        while start: 
            print('What would you like to display?')
            print()
            print('1 - Pilots with a license for a specific airplane')
            print('2 - All pilots sorted by license')
            print('3 - Single pilot information')
            print('m - Go back to display menu')
            print()

            selection = input()

            if selection == '1':
                #lista upp flugmenn með x leyfi

                pilot_license = input('Input license: ')
                
                return CrewUI().showByLicence(pilot_license)

                start = False


            elif selection == '2':
                # lista upp alla flugmenn eftir hvaða leyfi þeir hafa

                return CrewUI().showSortedByLicense()
                start = False

            elif selection == '3':
                pilot_ID = input('Input pilot ID: ')
                #lista upp ákveðinn flugmann
                return CrewUI().showOnePilot(pilot_ID)
                start = False

            elif selection == 'm':
                # fara aftur á display

                
                start = False
            else: 
                print('Invalid selection')