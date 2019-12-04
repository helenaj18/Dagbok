from API.LL_API import LL_API
import datetime

class SubMenuRegister: 
    def __init__(self, logic_layer): # muna ap taka inn logic layer sem main menu bjó til!!1!!!!!
        print('sub menu Register')
        self.logic_layer = logic_layer


    def startSubMenuRegister(self):
        print('#'*20)
        print('{:^20}'.format('REGISTER'))
        print('#'*20)
        print()

        print('What would you like to do?')
        print()

        while True:
            print('1 - Add new Employee')
            print('2 - Add new Voyage')
            print('3 - Add new Airplane')
            print('4 - Add new Destination')
            print('5 - Add staff to an available voyage')

            print('m - Main menu')
            print()

            selection = input()

            if selection == '1': 
                pass
            elif selection == '2':
                pass
            elif selection == '3':
                planeInsignia = input('Enter Insignia of the new plane (TF-XXX): ')
                planeTypeId = input('Enter planeTypeId:')

                LL_API().addAirplane(planeInsignia,planeTypeId)

            elif selection == '4':
                destination_of_voyage = input('Destination (3char airport code): ').upper()
                print('Departure time')
                dep_year = int(input('Year: '))
                dep_month = int(input('Month: '))
                dep_day = int(input('Day: '))
                dep_hour = int(input('Hour: '))
                dep_minute = int(input('Minute: '))
                departure_time = datetime.datetime(dep_year,dep_month,dep_day,dep_hour,dep_minute,0).isoformat()


                LL_API().add_voyage(destination_of_voyage,departure_time)

            elif selection == '5':
                pass
                
            elif selection == 'm':
                return

            else:
                print("Invalid selection")
                
