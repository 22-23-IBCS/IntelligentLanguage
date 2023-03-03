from graphics import*
from Button import*
class Hotel:
    def __init__(self,Hname,star):
        self.hn = Hname
        self.s = star

    def getHotel(self):
        return self.hn
    def getStar(self):
        return self.s

    
    

class Room(Hotel):
    def __init__(self,Hname,star,name,price,bedrooms,bathrooms,beds):
        super().__init__(Hname,star)
        self.n = name
        self.p = price
        self.be = bedrooms
        self.ba = bathrooms
        self.bed = beds
        
    def getName(self):
        return self.n
    def getPrice(self):
        return self.p
    def getBedrooms(self):
        return self.be
    def getBathrooms(self):
        return self.ba
    def getBeds(self):
        return self.bed

    def PriceSorting(a):
        
   
    
'''
class Hotel2:
    def __init__(self,Hname,star):
        self.hn = Hname
        self.s = star

    def getHotel(self):
        return self.hn
    def getStar(self):
        return self.s
    
        

class Room2(Hotel2):
    def __init__(self,Hname,star,name,price,bedrooms,bathrooms,beds):
        super().__init__(Hname,star)
        self.n = name
        self.p = price
        self.be = bedrooms
        self.ba = bathrooms
        self.bed = beds

    def getName(self):
        return self.n
    def getPrice(self):
        return self.p
    def getBedrooms(self):
        return self.be
    def getBathrooms(self):
        return self.ba
    def getBeds(self):
        return self.bed


class Hotel3:
    def __init__(self,Hname,star):
        self.hn = Hname
        self.s = star

    def getHotel(self):
        return self.n
    
        

class Room3(Hotel3):
    def __init__(self,Hname,name,price,bedrooms,bathrooms,beds):
        super().__init__(Hname)
        self.n = name
        self.p = price
        self.be = bedrooms
        self.ba = bathrooms
        self.bed = beds
'''
