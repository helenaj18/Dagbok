 
class AirplaneLL:
    ''' LL class for airplane '''
    def __init__(self, airplane, airplaneIO):
        self.airplane = airplane
        self.airplaneIO = airplaneIO
 
    def getAirplanes(self, num):
        '''Fetches list of airplanes and returns a list'''
        pass
   
    def addAirplane(self):
        pass



class Airplane:
    def __init__(self, name, seats, airplane_type):
        self.name = name
        self.seats = seats
        self.airplane_type = airplane_type