

class CrewLL:
 
    def __init__(self):
        pass
 
    def getCrew(self):
        ''' Gets the whole crew '''
        pilots = self.getPilots
        flight_att = IO_API().loadFlightAttFromFile()

        total_crew = pilots + flight_att

        # format a crew lagað...

        return total_crew

 
    def getPilots(self):
        ''' Gets pilot from all the pilots (crew)'''
        pilots = IO_API().loadPilotFromFile()

        #format a pilots lagað...

        return pilots
        
 
    def addPilot(self):
        ''' Adds pilot to pilots (crew)'''
        # input from UI layer
        new_pilot_str = LL_API().inputForNewPilot()


        # Format a str lagað...

        return new_pilot_str


 
    def editPilot(self):
        ''' Takes input from UI layer of info to edit, formats it and 
        sends to IO layer'''
        
        info_to_edit = LL_API().inputForEditedPilot()
        
        # format a list lagað ef þarf...

        return info_to_edit
 
    def addFlightAttendant(self):
        ''' Adds flight attendant to flight attendants (crew)'''
        info_to_add = LL_API().inputForNewFlightAtt()

        # format a info lagað...

        return info_to_add
 
    def editFlightAttendant(self):
        ''' Edits information of a flight attendant '''
        pass
 
    def getWorkingCrew(self):
        ''' Gets the working crew '''
        pass


class Crew:
    def __init__(self, name, crewID, address, landline, mobile, email):
        self.name = name
        self.crewID = crewID
        self.address = address
        self.landline = landline
        self.mobile = mobile
        self.email = email


class Pilot(Crew):
    def __init__(self, pilot_license, captain):
        self.pilotl_icense = pilot_license
        self.captain = captain
 
 
class FlightAttendant(Crew):
    def __init__(self, head_flight_att):
        self.head_flight_att = True