from IO.destinationIO import DestinationIO
from IO.crewIO import CrewIO
from IO.voyageIO import VoyageIO
from IO.airplaneIO import AirplaneIO
from IO.attendantIO import AttendantIO
from IO.pilotIO import PilotIO


class IO_API:
    '''API class for IO'''

    # DESTINATION 

    def loadDestinationFromFile(self):
        return DestinationIO().loadDestinationFromFile()

    def changeEmergencyPhone(self,destination_name,new_emergency_contact):
        return DestinationIO.changeEmergencyPhone()

    def changeEmergencyContact(self,destination_name,new_emergency_phone):
        return DestinationIO.changeEmergencyContact()

    def addDestinationToFile(self):
        return DestinationIO.addDestinationToFile()


    #CREW

    def loadCrewFromFile(self):
        return CrewIO().loadCrewFromFile()

    def loadPilotFromFile(self):
         return PilotIO().loadPilotFromFile()
    
    def loadFlightAttFromFile(self):
         return AttendantIO().loadFlightAttFromFile()

    def changeCrewInfo(self,employee):
        return CrewIO().changeCrewFile(employee)


    def changeCrewFile(self,updatedPilot):
        return CrewIO().changeCrewFile(updatedPilot)


    def addPilot(self, new_employee_str):
        return CrewIO().addPilotToFile(new_employee_str)

    
    def addCrew(self, new_employee_str):
        return CrewIO().addCrewToFile(new_employee_str)
 



    # VOYAGES

    def loadVoyageFromFile(self):
        return VoyageIO().loadVoyageFromFile()
    
    # def read_file(self):  EKKI Í NOTKUN 
    #     return VoyageIO().read_file()


    def changeVoyageFile(self,voyage):
        return VoyageIO().changeVoyageFile(voyage)


    def addVoyageToFile(self,new_voyage_str):
        return VoyageIO().addVoyageToFile(new_voyage_str)


    # VOYAGE

    def loadAirplaneFromFile(self):
        return AirplaneIO().loadAirplaneFromFile()


    def changeAirplaneInFile(self):
        return AirplaneIO().change_airplane_in_file()


    def addAirplaneToFile(self,planeInsignia,planeTypeId,manufacturer,seats):
        return AirplaneIO().addAirplaneToFile(planeInsignia,planeTypeId,manufacturer,seats)
