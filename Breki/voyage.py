import datetime

class flight:
    def __init__(self,distance,TimeOfArrival):
        self.distance = distance
        self.TimeOfArrival = TimeOfArrival
    def displaydistance(self):
        print(self.distance)

    def display_TimeofArrival(self):
        print(self.TimeOfArrival)



class voyage(flight):
    def __init__(self):
        

        
    def doubleDistance(self):
        doubledistance = self.distance * 2
        print(self.doubleDistance)
    
    #def doubleTimeofArrival(self):
    #    print(self.doubleTimeOfArrival)


test = flight(123,123)
test.display_doubleDistance
