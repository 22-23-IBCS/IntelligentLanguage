import random
    
class House:
    def __init__ (self):
        self.r = random.randint(1,10)

    def getV(self):
        return self.r
    def setV(self):
        #if the house is already visited, set generosity to 0
        self.r=0
    

    def adjacent(self,x,y,Hmap):
        #limit x, y value so it will not be out of range
        #if it's out of range, set the generosity to -1, so it won't be the maximum anyway.
        if y <=3:
            a = Hmap[x][y+1].getV()
        else:
            a = -1
        if x<=3:
            b = Hmap[x+1][y].getV()
        else:
            b = -1
        if y>=1:
            c = Hmap[x][y-1].getV()
        else:
            c = -1
        if x >=1:
        
            d = Hmap[x-1][y].getV()
        else:
            d = -1
    
        neighbor = [a,b,c,d]
        #return a list that includes generosity of the house and its x, y values
        if neighbor.index(max(neighbor)) == 0:
            return [a,x,y+1]
        elif neighbor.index(max(neighbor)) == 1:
            return [b,x+1,y]
        elif neighbor.index(max(neighbor)) == 2:

            return [c,x,y-1]
        elif neighbor.index(max(neighbor)) == 3:
            return [d,x-1,y]


        
            
            
    
        
def main():
    #create and print the map
    housemap = []
    for j in range(5):
        h = []
        people = []
        for i in range(5):
            people.append(House())
            h.append(people[i].getV())
        housemap.append(people)
        print(h)

    #users questions
    numHouse = int(input("Input a integer that indicates how many houses you plan to visit\n"))
    start1 = int(input("Where do you want to start? X value(0-4):\n"))
    start2 = int(input("Y value(0-4):\n"))
    
        
    print("bottom are the generosity of houses and its coordinates")
    
    #first starting houses
    

    #calculate total average
    total1 = 0
    for i in range(5):
        for j in range(5):
            total1 = total1 + housemap[i][j].getV()
    ave1 = total1/25
    total = 0
    for i in range(numHouse):
        n = housemap[start1][start2].getV()
        total = total + n    #calculate average of houses visited
        lo = [housemap[start1][start2].getV(),start1,start2]
        print(lo)

        lo = housemap[start1][start2].adjacent(start1,start2,housemap) #find next house to visit
        housemap[start1][start2].setV() #set the house that has already been visited to -10000
        start1 = lo[1] #reset the position of user and ready to find next adjacent
        start2 = lo[2]    
    ave = total/numHouse
    
    print("Average val of all houses is: ")
    print(ave1)
    print("Average val of path is: ")
    print(ave)

        
    
    


if __name__ == "__main__":
    main()
