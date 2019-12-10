class Destination():
    def __init__(self,distance = 0.0,city = "", country = "", emergencycontact = ""):
        self.distance = distance
        self.city = city
        self.country = country
        self.emergencycontact = emergencycontact
    
    def updateEmergencyContact(self):
        pass

    def storeFlightLength(self):
        pass
    
    def __str__(self):
        return "Distance: {}, City: {}, Country: {}, Emergencycontact: {}"\
            .format(self.distance, self.city, self.country, self.emergencycontact)
