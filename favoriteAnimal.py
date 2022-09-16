class FavAni:
    def __init__(self,name,t,col,f,s):
        self.name = name
        self.type = t
        self.color = col
        self.food = f
        self.sleep = s
        
     
    def setColor(self,col):
        self.color = col

    def getColor(self):
        return self.color
    def getType(self):
        return self.type


    


def main():

    ani1 = FavAni("cat", "Ragdoll","white","fish","8")
    ani2 = FavAni("dog","Alaskan Malamute", "white", "sausage","5")
    print("One of my favorite animal is "+ani1.getType())
    print("One of my favorite animal is "+ ani2.getType())
    print("The origial color of the animal is "+ ani1.getColor() )
    b = ani1.setColor("red")
    print("The current color of the animal is " +ani1.getColor())

    
    

if __name__ == "__main__":
    main()
