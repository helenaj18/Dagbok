from API.LL_API import LL_API
from LL.airplaneLL import AirplaneLL
from LL.crewLL import CrewLL
import datetime
from ModelClasses.flight_att_model import FlightAttendant
from ModelClasses.pilot_model import Pilot


class CrewUI:

    def __init__(self):
        self.BANNER_pilot = '{:<25}{:<20}{:<25}{:<10}\n'.format('Name', 'Pilot ID', 'Rank', 'License')
        self.BANNER_pilot += '_'*80
        self.BANNER_att = '{:<25}{:<20}{:<20}\n'.format('Name', 'Flight Att. ID', 'Rank')
        self.BANNER_att += '_'*80
        self.BANNER_crew = '{:<25}{:<20}{:<25}{:<20}\n'.format('Name','Crew Member ID','Rank','License')
        self.BANNER_crew += '_'*80
    def __str__(self):
        pass 
    
    def showCrew(self):
        '''' Shows full list of crew, pilots and flight attendants'''
        crew = LL_API().get_crew()
        string = ''

        print(self.BANNER_pilot)

        for employee in crew:
            string = '{:<25}{:<20}'.format(employee.getName(),employee.getCrewID())

            if type(employee) == Pilot:
                if employee.getBool():
                    string += '{:<25}{:<10}'.format('Captain', employee.getLicense())
                else:
                    string += '{:<25}{:<10}'.format('Co-pilot', employee.getLicense())
            else:
                if employee.getBool():
                    string += '{:<15}'.format('Head service manager')
                else:
                    string += '{:<15}'.format('Flight attendant')
            
            print(string)

        print()
    

    def showWorkingCrew(self,date_str):
        format_str = LL_API().get_working_crew(date_str)
        print(format_str)
        self.printCrew(format_str,True)


    def showNotWorkingCrew(self,date_str):
        not_working_crew_list = LL_API().get_not_working_crew(date_str)
        self.printCrew(not_working_crew_list, False)

    def queryShowNotWorkingCrew(self, date_str):
        self.showNotWorkingCrew(date_str)
        keep_asking = True
        while keep_asking:
            customer_input = input("What staff member do you want to pick from the list above (Employee ID): ")
            employee = CrewLL().getOneCrewMember(customer_input)
            if employee:
                return employee
            print("Employee not found, try again")
        
        #  for crew_member in not_working_crew_list:
        #         format_str += '{:<15}{:<20}{:<20}{:<10}{:<10}{:<20}\n'.format(
        #             crew_member.getRole(),
        #             crew_member.getName(),
        #             crew_member.getCrewID(),
        #             crew_member.getBool(),
        #             crew_member.getEmail(),
        #             crew_member.getPhoneNumber()
        #         )


    def printCrew(self,not_working_crew_list, not_working):
        header = 'Working Crew' if not_working else 'Not Working crew'
        if not_working_crew_list != None:
            print('#'*30)
            print('{:^30}'.format(header))
            print()
            print('#'*30)
            header_str = '{:<20}{:<20}{:<20}{:<20}{:<20}{:<10}'.format(
                'Role','Name','Employee Id','Position','Email',\
                    'Phone Number','Destination')

            print(header_str)
            print(len(header_str)*'-')
            for crew_member in not_working_crew_list:
                role = crew_member.getRole()
                if role == 'Pilot':
                    if crew_member.getBool(): 
                        position = 'Captain'
                    else: 
                        position = 'Pilot'
                elif role == 'Cabincrew':
                    if crew_member.getBool(): 
                        position = 'Head'
                    else: 
                        position = 'Flight Att.'

                format_str += '{:<15}{:<20}{:<20}{:<10}{:<10}{:<20}\n'.format(
                    crew_member.getRole(),
                    crew_member.getName(),
                    crew_member.getCrewID(),
                    position,
                    crew_member.getEmail(),
                    crew_member.getPhoneNumber()
                )
                print(format_str)


            print()
        else:
            print('\nNo voyages on this day\n')



    def changeEmployeeInfo(self,employee):
        LL_API().changeCrewInfo(employee)


    def changePilotLicense(self,crew_id,new_license):
        LL_API().changePilotLicense(crew_id,new_license)

            
    def showOneCrewMember(self,crew_id):
        crew_member = LL_API().get_crew_member_by_id(crew_id)
        print('-'*50)

        if crew_member == None:
            print('Employee with this id not found!')
            print()
            return False
        else:
            print('Name: {}'.format(crew_member.getName()))
            print('SSN: {}'.format(crew_member.getCrewID()))
            print('Address: {}'.format(crew_member.getAddress()))
            print('Phone number: {}'.format(crew_member.getPhoneNumber()))
            print('Email: {}'.format(crew_member.getEmail()))

            if type(crew_member) == Pilot:
                if crew_member.getBool():
                    print('Rank: Captain')
                    print('License: {}'.format(crew_member.getLicense()))
                else:
                    print('Rank: Co-pilot')
                    print('License: {}'.format(crew_member.getLicense()))
            else:
                if crew_member.getBool():
                    print('Rank: Head service manager')
                else:
                    print('Rank: Flight attendant')

            print()
            return True


    def showAllPilots(self):
        ''' Shows full list of pilots registered'''
        return LL_API().get_pilots()


    def showByLicense(self, license_ID):
        ''' Shows a list of pilots that have a specific licence '''

        licensed_pilots_list = LL_API().get_licensed_pilots(license_ID)

        print(self.BANNER_pilot)

        for pilot_instance in licensed_pilots_list:
            
            if pilot_instance.getBool():
                rank = 'Captain'
            else:
                rank = 'Copilot'

            print('{:<25}{:<20}{:<25}{:<10}'.format(pilot_instance.getName(), pilot_instance.getCrewID(), rank, pilot_instance.getLicense()))

        print()

    def showSortedByLicense(self):
        '''Shows a list of all pilots sorted by license'''

        sorted_pilots_list =  LL_API().sortPilotsByLicense()

        print(self.BANNER_pilot)
        
        for pilot in sorted_pilots_list:
            
            if pilot.getBool():
                rank = 'Captain'
            else:
                rank = 'Copilot'

            print('{:<25}{:<20}{:<25}{:<10}'.format(pilot.getName(), pilot.getCrewID(), rank, pilot.getLicense()))
    
        print()

    def showAllFlightAtt(self):
        ''' Shows a full list of all pilots registered''' 
        
        print(self.BANNER_att)

        flight_att = LL_API().get_flight_att()

        for attendant in flight_att:

            if attendant.getBool():
                rank = 'Head service manager'
            else:
                rank = 'Flight attendant'

            print('{:<25}{:<20}{:<20}'.format(attendant.getName(), attendant.getCrewID(), rank ))
        print()

    def addCrew(self):
        info_list = []
        print('Please fill in the following information. Press enter to skip.\n')

        info_list.append(input('Personal ID (required): '))
        info_list.append(input('Name (required): '))

        print('Please choose one of the following job titles:')
        print('1 - Captain')
        print('2 - Co-pilot')
        print('3 - Head service manager')
        print('4 - Flight attendant')
        rank = input()
        while rank != '1' and rank != '2' and rank != '3' and rank != '4':
            print('Please choose a number between 1-4')
            rank = input()
                
        info_list.append(rank)

        if rank == '1' or rank =='2':
            info_list.append( input('Pilot license: ') )

        info_list.append( input('Home address: ') )
        info_list.append( input('Phone number: ') )
        info_list.append( input('Email: ') )

        LL_API().addCrew(info_list)

        #info_list for pilots is longer because of license

        print('New Employee added!\n') 
        

    def showSchedule(self, crew_ID):
        ''' Shows the schedule for a specific crew member '''
        employee = LL_API().get_crew_member_by_id(crew_ID)
        
        if employee != None:
            print('Enter the "From date" for the work schedule')
            
            start_year_str = input('Year: ')
            start_month_str = input('Month: ')
            start_day_str = input('Day: ')

            start_year_int, start_month_int, start_day_int = AirplaneLL().verifyDate(start_year_str, start_month_str, start_day_str)
            start_date = datetime.datetime(start_year_int,start_month_int,start_day_int,0,0,0).isoformat()
            
            print('Enter the "To date" for work schedule')
            end_year_str = input('Year: ')
            end_month_str = input('Month: ')
            end_day_str = input('Day: ')

            end_year_int, end_month_int, end_day_int = AirplaneLL().verifyDate(end_year_str, end_month_str, end_day_str)
            end_date = datetime.datetime(end_year_int,end_month_int,end_day_int,0,0,0).isoformat()
            
            work_schedule_list = LL_API().get_work_schedule(start_date,end_date,crew_ID)
            
        
            name_header_str = '{:<10} {:<10}'.format(employee.getName(),crew_ID)
            header_str = 'Working Schedule {}.{}.{}-{}.{}.{}'.format(start_day_int,start_month_int,start_year_int,end_day_int,end_month_int,end_year_int)
            print()
            print(name_header_str)
            print(header_str)
            print(len(header_str)*'-')

            if work_schedule_list != None: 
                for voyage in work_schedule_list:
                    flight_no_out,flight_no_home = voyage.getFlightNumbers()
                    voyage_duration_hrs, voyage_duration_min = LL_API().get_voyage_duration(voyage)
                    aircraft_ID = voyage.getAircraftID()
                    self.prettyprint(voyage,flight_no_out,flight_no_home,voyage_duration_hrs,voyage_duration_min,\
                    aircraft_ID)
                return True
            else:
                print('No voyages in this time period\n')
                return True
        else:
            return False
            
    def prettyprint(self,voyage,flight_no_out,flight_no_home,voyage_duration_hrs,voyage_duration_min,\
        aircraft_ID):

        print('To {}, {} on {} at {}'.format(voyage.getDestination().getDestinationName(), voyage.getDestination().getDestinationAirport(),\
                voyage.getDepartureTime()[:10] ,voyage.getDepartureTime()[-8:-3]))
        print('\t Flight numbers: {} - {}'.format(flight_no_out, flight_no_home))
        print('\t Total time: {} hrs {} min'.format(voyage_duration_hrs,voyage_duration_min))
        print('\t Aircraft: {}'.format(aircraft_ID))

