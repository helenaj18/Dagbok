
class Voyage:
    def __init__(self,voyage_ID,flight_no,flight_no_home,departure_location,destination,\
                    departure_time,arrival_time_out,arrival_time_home,aircraft_ID,captain,copilot,\
                        head_flight_att,flight_att_one,flight_att_two):

        self.__voyage_ID = voyage_ID
        self.__flight_no_out = flight_no
        self.__flight_no_home = flight_no_home
        self.__departure_location = departure_location
        self.__destination = destination
        self.__departure_time = departure_time
        self.__arrival_time_out = arrival_time_out
        self.__arrival_time_home = arrival_time_home
        self.__aircraft_ID = aircraft_ID
        self.__captain = captain
        self.__copilot = copilot
        self.__head_flight_att = head_flight_att
        self.__flight_att_one = flight_att_one
        self.__flight_att_two = flight_att_two
        

    def getDepartureTime(self):
        return self.__departure_time

    def getArrivalTimeOut(self):
        return self.__arrival_time_out
        
    def getArrivalTimeHome(self):
        return self.__arrival_time_home

    def getCrewOnVoyage(self):
        crew_on_voyage_list = [self.__captain, self.__copilot, self.__head_flight_att,\
            self.__flight_att_one, self.__flight_att_two]
        return crew_on_voyage_list

    def getFlightNumbers(self):
        return self.__flight_no_out, self.__flight_no_home

    def getDestination(self):
        return self.__destination

    def getAircraftID(self):
        return self.__aircraft_ID

    # def getDestinationName(self):
    #     return self.__destination_name

    def getVoyageID(self):
        return self.__voyage_ID
    


    def __str__(self):
        a_string = str(self.__voyage_ID) +',' + str(self.__flight_no)
    
        return a_string


    # SET METHODS
    def setDepartureTime(self, new_time):
        self.__departure_time = new_time
    
    def setArrivalTime(self, new_time):
        self.__arrival_time = new_time
    
    def setAircraftID(self, new_id):
        self.__aircraft_ID = new_id
    
    def setCaptain(self, new_capt):
        
        airplane_type = "NAFokkerF28" ##taka út harðkóðun
        if not new_capt.canFly(airplane_type):
            raise Exception("Pilot can not fly this type")
    
        self.__captain = new_capt
    
    def setCopilot(self, new_copilot):
        
        airplane_type = "NAFokkerF28" ##taka út harðkóðun
        if not new_copilot.canFly(airplane_type):
            raise Exception("Copilot can not fly this type")
    
        self.__copilot = new_copilot
    
    def setHeadFlightAtt(self, new_head):
        self.__head_flight_att = new_head

    def setFlightAttOne(self, new_att):
        self.__flight_att_one = new_att
    
    def setFlightAttTwo(self, new_att):
        self.__flight_att_two = new_att

    def setPilot(self, pilot):
        if pilot.isCaptain():
            self.setCaptain(pilot)
        else:
            self.setCopilot(pilot)

    def addCrewMember(self, crew_member):
        role = crew_member.getRole()
        if role == "Pilot":
            self.setPilot(crew_member)
        elif role == "Flightasdfasd":
            pass
