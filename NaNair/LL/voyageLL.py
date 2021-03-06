from API.IO_API import IO_API
from IO.voyageIO import VoyageIO
from LL.airplaneLL import AirplaneLL
from LL.destinationLL import DestinationLL
import datetime

class VoyageLL:
    ''' LL class for voyage '''

    # When a new voyage is added there are no sold seats
    seats_sold_out = '0'
    seats_sold_home = '0'

    
    def getUpcomingVoyages(self):
        '''Returns a list of instances of all future voyages'''
        
        # all voyages
        voyage_list = IO_API().loadVoyageFromFile()
        date_today =  datetime.date.today()
        upcoming_voyages_list = []
    
        for voyage in voyage_list: 
            # datetime of voyage instance
            voyage_departure_datetime = AirplaneLL().revertDatetimeStrtoDatetime(voyage.getDepartureTime())
            voyage_departure_date = voyage_departure_datetime.date()
            # if departure of voyage is in the future
            if voyage_departure_date >= date_today:
                upcoming_voyages_list.append(voyage)

        return upcoming_voyages_list
                 
        

    def getOneVoyage(self, voyage_to_get_ID_str):
        '''Takes in voyage id and returns the voyage class instance that has that id'''
        
        # all voyages
        voyage_instance_list = IO_API().loadVoyageFromFile()
        
        for voyage_instance in voyage_instance_list:
            # if inputted ID is the same as ID of voyage
            voyage_ID_str = voyage_instance.getVoyageID()
            if voyage_ID_str == voyage_to_get_ID_str: 
                return voyage_instance

        # if no instance is returned        
        return None
                


    def getVoyageDuration(self,voyage_instance):
        ''' Takes in voyage instance.
        Returns voyage duration in hours and minutes'''
        
        # duration of one way trip. Format: xxhxxm where xx are numbers
        duration_str = voyage_instance.getDestination().getDestinationDuration()

        # hrs and mins isolated
        duration_hrs_int = int(duration_str[: -4])
        duration_minutes_int = int(duration_str[-3: -1])
        voyage_duration_min_int = duration_minutes_int * 2

        # Duration of round trip plus 1 hour layover
        voyage_duration_hrs_int = duration_hrs_int * 2 + 1 

        # if minutes are exactly an hour
        if voyage_duration_min_int == 60:
            voyage_duration_hrs_int = voyage_duration_hrs_int + 1
            voyage_duration_min_int = 0 

        # if minutes are more than an hour
        elif voyage_duration_hrs_int > 60: 
            voyage_duration_hrs_int = voyage_duration_hrs_int + 1
            voyage_duration_min_int = voyage_duration_min_int - 60 

        return voyage_duration_hrs_int, voyage_duration_min_int


    def isEmployeeWorkingOnDate(self, date, employee_id):
        '''Checks if an inputted employee is working on an inputted date.
        Returns True if he is, else False.'''

        # all voyages on inputted date
        voyages_intstance_list = self.getVoyageInDateRange(daBte, date)
        
        for voyage in voyages_intstance_list:
            # if employee is assigned to voyage
            if employee_id in voyage.getCrewOnVoyage():
                return True
        return False


    def getVoyageStatus(self, voyage_instance):
        '''Takes a voyage instance and checks its status based on current time. A string describing 
        the status is returned.'''

        time_now_datetime = datetime.datetime.now()

        # departing and arriving time of flight at KEF
        voyage_depart_time_home_str = voyage_instance.getDepartureTime()
        voyage_arrive_time_home_str = voyage_instance.getArrivalTimeHome()

        # departing and arriving time of flight at destination
        voyage_arrive_time_out_str = voyage_instance.getArrivalTimeOut()
        voyage_depart_time_out_str = voyage_instance.getDepartureTimeAtDestination()
        
        # Turn depart and arrive time string into a datetime value
        voyage_depart_home_datetime = AirplaneLL().revertDatetimeStrtoDatetime(voyage_depart_time_home_str)
        voyage_arrive_home_datetime = AirplaneLL().revertDatetimeStrtoDatetime(voyage_depart_time_home_str)

        voyage_depart_out_datetime = AirplaneLL().revertDatetimeStrtoDatetime(voyage_depart_time_out_str)
        voyage_arrive_out_datetime = AirplaneLL().revertDatetimeStrtoDatetime(voyage_depart_time_out_str)

        # if voyage departed before current time
        if time_now_datetime < voyage_depart_home_datetime:
            status_str = 'Not departed'
        # if voyage departed before current time but has not yet arrived out OR if it has departed back home and hasnt arrived
        elif (time_now_datetime >= voyage_depart_home_datetime and time_now_datetime < voyage_arrive_out_datetime)\
            or (time_now_datetime >= voyage_depart_out_datetime and time_now_datetime < voyage_arrive_home_datetime):
                status_str = 'In air'
        # if voyage has landed in destination but not departed back
        elif time_now_datetime >= voyage_arrive_out_datetime and time_now_datetime < voyage_depart_out_datetime:
            status_str = 'At destination'
        # if voyage has arrived    
        else:
            status_str = 'Completed'
        
        return status_str

    def addCaptain(self, voyage_id, date, employee_id):
        '''Captain added to an existing voyage'''

        # check if employee is working on inputted date
        is_unavailable_bool = self.isEmployeeWorkingOnDate(date, employee_id)
        
        if is_unavailable_bool:
            raise Exception("Staff member not available on this date")
        
        voyage_instance = VoyageIO.getOneVoyage(voyage_id)
        if voyage_instance is None:
            raise Exception("Voyage not found")
        # captain added to voyage instance
        voyage_instance.setCaptain(employee_id)


    def getVoyageInDateRange(self, start_datetime, end_datetime):
        ''' Returns a list of instances of all voyages in a certain date range'''

        # all voyages
        voyages_instance_list = IO_API().loadVoyageFromFile()

        voyages_on_date_list = []
        list_of_dates = []
        # value to add a day to datetime object
        delta = datetime.timedelta(days=1)

        # make a list of all dates between start and end time
        while start_datetime <= end_datetime:
            list_of_dates.append(start_datetime.date().isoformat())
            start_datetime += delta

        # change date format to string and check if depart or arrive time is in list of times
        for voyage in voyages_instance_list:
            departure_datetime = voyage.getDepartureTime()
            departure_date = departure_datetime[:10]

            arrival_datetime = voyage.getArrivalTimeHome()
            arrival_date = arrival_datetime[:10]

            if departure_date in list_of_dates:
                voyages_on_date_list.append(voyage)

            elif arrival_date in list_of_dates:
                voyages_on_date_list.append(voyage)

        return voyages_on_date_list
    
    def getCompletedVoyagesInRange(self, start_datetime, end_datetime):
        '''Gets a list of completed voyages in a date range'''
        
        # all voyages in date range
        voyages_on_date = self.getVoyageInDateRange(start_datetime, end_datetime)
        completed_voyage_list = []

        # make list of voyages which have status as completed
        for voyage in voyages_on_date:
            if self.getVoyageStatus(voyage) == 'Completed':
                completed_voyage_list.append(voyage)
        
        return completed_voyage_list
            

    def assignVoyageID(self):
        '''Assign a voyage an id based on last voyage in file.'''
        
        # Get voyage id of last voyage in file
        voyage_list = IO_API().loadVoyageFromFile()
        last_voyageID_str = voyage_list[-1].getVoyageID()
 
        new_id_int = int(last_voyageID_str) + 1
        return str(new_id_int)
 

    def assignFlightNo(self, destination, depart_time):
        '''Assigns a departing and arriving flight number based on a location
        and other trips that day.'''
    
        # first two letters are dictated by destination
        if destination == 'LYR':
           first_two = '01'
        elif destination == 'GOH':
           first_two = '02'
        elif destination == 'KUS':
           first_two = '03'
        elif destination == 'FAE':
           first_two = '04'
        else:
           first_two = '05'
        
        # all voyages on departing day
        voyage_list = self.getVoyageInDateRange(depart_time, depart_time)

        # if no voyages are on the departing day
        latter_two_depart = '00'
        latter_two_arrive = '01'

        for voyage_instance in voyage_list:

            voyage_instance_depart_time = AirplaneLL().revertDatetimeStrtoDatetime( voyage_instance.getDepartureTime() )
            # if the dest IATA code matches the voyage in file there is another voyage to 
            # the same destination on the same day
            if destination == voyage_instance.getDestination().getDestinationAirport():
                if depart_time >= voyage_instance_depart_time:
                    # flight numbers of registered voyage:
                    depart_num, arrival_num = voyage_instance.getFlightNumbers()

                    # if the registered voyage has higher numbers
                    if latter_two_depart <= depart_num[-2:]:
                        latter_two_depart = str( int(depart_num[-2:]) + 2 )
                        latter_two_arrive = str( int(arrival_num[-2:]) + 2 )
                    # int() removes the zero so it is added back in
                    if len(latter_two_depart) == 1:
                        latter_two_depart = '0' + latter_two_depart
                        latter_two_arrive = '0' + latter_two_arrive
                else:
                    # change flight number of old voyage
                    self.changeFlightNo(voyage_instance)
                    departing_num, arriving_num = voyage_instance.getFlightNumbers()


        departing_num = 'NA' + first_two + latter_two_depart
        arriving_num = 'NA' + first_two + latter_two_arrive

        return departing_num, arriving_num


    def changeFlightNo(self, voyage_instance):
        '''Changes flight number of later voyages if a new voyage is added earlier time'''
        
        #flight numbers
        depart_num, arrival_num = voyage_instance.getFlightNumbers()

        # add 2 to the numbers
        latter_two_depart = str( int(depart_num[-2:]) + 2 )
        latter_two_arrive = str( int(arrival_num[-2:]) + 2 )

        # zero is removed in int() so it is added back if needed
        if len(latter_two_depart) == 1:
            latter_two_depart = '0' + latter_two_depart
            latter_two_arrive = '0' + latter_two_arrive

        # new numbers
        new_depart_num = depart_num[:-2] + latter_two_depart
        new_arrival_num = arrival_num[:-2] + latter_two_arrive

        # add new numbers to instance
        voyage_instance.setDepartNum(new_depart_num)
        voyage_instance.setArrivalNum(new_arrival_num)

        # load to file
        IO_API().changeVoyageFile(voyage_instance)



    def TimeDifference(self, time_datetime, dest_code):
        '''Calculates time difference between KEF and destinations'''
        
        if dest_code == 'LYR':
            time_datetime = time_datetime + datetime.timedelta(hours=1)
        elif dest_code == 'GOH' or dest_code == 'KUS':
            time_datetime = time_datetime + datetime.timedelta(hours=-3)

        # time in faroe islands (FAE) and tingwall (LWK) is gmt so no need to change

        return time_datetime


    def findArrivalTime(self, dest_code, depart_time_datetime):
        '''Takes in destination code and departure time and returns arrival time at
        destination as datetime object.'''

        destinations_instances = DestinationLL().getDestination()
        duration_str = ''

        # finds duration of flight to destination as string
        for destination in destinations_instances:
            if dest_code == destination.getDestinationAirport():
                duration_str = destination.getDestinationDuration()
        
        # turns duration string into int values, form of string is xxhxxm where x are numbers
        index_of_h_int = duration_str.find('h')

        if index_of_h_int == 1:    
            hrs_int = int(duration_str[0])
        else:
            hrs_int = int(duration_str[ :(index_of_h_int - 1) ])
        mins_int = int(duration_str[(index_of_h_int + 1):3])
        
        arrival_time_datetime = depart_time_datetime + datetime.timedelta(hours=hrs_int, minutes=mins_int)

        return arrival_time_datetime


    def getAvailablePlanes(self, departure_time, arrival_time):
        '''Finds which planes are available at departing and arriving time. Returns list of instances of 
        available planes.'''
        
        available_tuples_by_time = []
        # value to increase datetime object in each loop
        delta = datetime.timedelta(hours=0.1)

        # list of tuples which show available planes at each time between departure and arrival
        while departure_time <= arrival_time:
            available_tuples_by_time.append( AirplaneLL().getAirplanesByDateTime(departure_time) )
            departure_time += delta    

        all_airplanes = AirplaneLL().getAirplanes()
        not_available_planes_insignia = []
        available_planes = []

        for available_tuple in available_tuples_by_time:
            if available_tuple != None: # if available tuple is None there are no unavailable planes
                not_available_planes_at_time,available_planes_at_time = available_tuple

                # add unavailable planes to list
                for item in not_available_planes_at_time:
                    if item[0].get_planeInsignia() not in not_available_planes_insignia:
                        not_available_planes_insignia.append(item[0].get_planeInsignia())

        # create list af available planes by comparing all planes to unavailable planes
        for plane in all_airplanes:
            if plane.get_planeInsignia() not in not_available_planes_insignia:
                available_planes.append(plane)
        
        return available_planes



    def checkPlaneInput(self, plane_input, list_of_plane_instances):
        '''Checks if inputted plane exists in inputted list of available planes'''

        BoolCheck = False
        for plane in list_of_plane_instances:
            if plane_input == plane.get_planeInsignia():
                BoolCheck = True
        
        return BoolCheck

 
    def findArrivalTimeHome(self, departure_datetime, dest):
        '''Finds arrival time home based on location and destination'''

        # arrival time at destination in gmt
        arrival_time_gmt = self.findArrivalTime(dest, departure_datetime)
        # arrival time at destination at local time
        arrival_time_out = self.TimeDifference(arrival_time_gmt, dest)

        departure_time_back = arrival_time_out + datetime.timedelta(hours=1)
        
        # arrival time in iceland
        arrival_time_back = self.findArrivalTime(dest, departure_time_back)

        return arrival_time_back


    def addVoyage(self,destination, departure_time, plane):
        '''Finds values from input to register a new voyage. Returns a list with all info.'''    
    
        voyage_id = self.assignVoyageID()

        # Flight numbers
        flight_depart_num, flight_arrive_num = self.assignFlightNo(destination, departure_time)

        # arrival time in other country added, time difference taken into account
        arrival_time_gmt = self.findArrivalTime(destination, departure_time)
        arrival_time_out = self.TimeDifference(arrival_time_gmt, destination)

        # plane stops at destination for 1 hour 
        departure_time_back = arrival_time_out + datetime.timedelta(hours=1)

        arrival_time_back = self.findArrivalTimeHome(departure_time,destination)

        # info added to list in same order as in allvoyages.csv
        info_list = [voyage_id, flight_depart_num, self.seats_sold_out, 'KEF', destination,\
                    departure_time.isoformat(), arrival_time_out.isoformat(),\
                    flight_arrive_num, self.seats_sold_home, destination, 'KEF',\
                    departure_time_back.isoformat(), arrival_time_back.isoformat(),\
                    plane]

        # staff not yet added so those values will be empty
        for i in range(5):
            info_list.append('empty')
        
        new_voyage_str = ','.join(info_list)

        IO_API().addVoyageToFile(new_voyage_str)


    def checkDestInput(self, dest_input):
        '''Checks if destination IATA code is valid. Returns true if it is valid, else false'''

        # all destinations
        destinations_instances = DestinationLL().getDestination()
        boolOutcome = False

        # if input is of correct length
        if len(dest_input) == 3:
            for destination in destinations_instances:
                # if input matches any of the dest codes
                if dest_input == destination.getDestinationAirport():
                    boolOutcome = True
        
        return boolOutcome

    def checkIfTakenTime(self, departure_datetime):
        '''Checks if date inputted by user is taken by another voyage. 
        Returns true if its taken, else false'''

        taken = False
        datetime_list = []

        # assume one plane can leave each half hour
        start_time = departure_datetime + datetime.timedelta(minutes=-30)
        end_time = departure_datetime + datetime.timedelta(minutes=30)

        # list of voyages that depart the same day
        voyages_during_departure_date = self.getVoyageInDateRange(start_time, end_time)

        # list of all times in restricted hour
        while start_time <= end_time:
            datetime_list.append(start_time.isoformat())
            start_time += datetime.timedelta(minutes=1)

        # if a voyage that departs the same day as inputted voyage is also in datetime_list
        # it is too close in time
        for voyage in voyages_during_departure_date:
            if voyage.getDepartureTime() in datetime_list:
                taken = True
            elif voyage.getArrivalTimeHome() in datetime_list:
                taken = True
        
        return taken


    def changeSoldSeats(self,voyage,flight_str,new_seats_str):
        '''Takes in voyage instance, string that dictates which flight is being changed (home or out),
        and string of new seats number'''
        all_airplanes = IO_API().loadAirplaneFromFile()

        airplane_id = voyage.getAircraftID()
        
        if airplane_id != 'empty':
            # get total seats of plane
            for airplane in all_airplanes:
                if airplane.get_planeInsignia() == airplane_id:
                    total_seats = airplane.get_planeCapacity()
            
            while True:
                # if sold seats are fewer than total seats
                if int(new_seats_str) <= int(total_seats):

                    if flight_str == 'home':
                        voyage.setSeatsSoldHome(new_seats_str)
                    else:
                        voyage.setSeatsSoldOut(new_seats_str)

                    return IO_API().changeVoyageFile(voyage)
                else:
                    print('Invalid input! The airplane only has {} seats!'.format(int(total_seats)))
        
        else:
            print('\nNo aircraft has been assigned to the voyage, please add an aircraft first!\n')


    def changeVoyageFile(self,voyage):
        '''Sends class instance of updated employee into IO layer to read into file'''
        return IO_API().changeVoyageFile(voyage)





