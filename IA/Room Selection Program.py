from graphics import*
from Button import*
from Hotel import*



def main():
    Hotelone = Hotel("Beijing Double Happiness Courtyard Hotel",3)
    Hoteltwo = Hotel("InterContinental Beijing Beichen, an IHG Hotel",5)
    Room11 = Room("Beijing Double Happiness Courtyard Hotel",3,"Chinese-style Deluxe Double Room",101, 1, 1, 1)
    Room12 = Room("Beijing Double Happiness Courtyard Hotel",3,"Chinese-style Deluxe Twin Room", 101, 1, 1, 2)
    Room13 = Room("Beijing Double Happiness Courtyard Hotel",3,"Superior Family Room", 151, 2,2,3)
    Room21 = Room("InterContinental Beijing Beichen, an IHG Hotel",5,"1 King Bed Premium Birds Nest View", 298, 1, 1, 1)
    Room22 = Room("InterContinental Beijing Beichen, an IHG Hotel",5,"1 King Bed Premier Suite", 597, 2, 1, 1)
    print(Hotelone.getHotel())
    
    win = GraphWin("Hotel Rating Program",1300,800)
    title = Text(Point(650,20), "Hotel Rating Program") 
    title.setSize(32)
    title.draw(win)


    maxPrice = Text(Point(1050,150), "Enter maximum price($), enter NA if you don't care")
    maxPrice.draw(win)
    maxPrice.setSize(20)
    minStar = Text(Point(1050,250), "Enter minimum star, enter NA if you don't care")
    minStar.draw(win)
    minStar.setSize(20)
    numBe = Text(Point(1050,350), "Enter number of bedroom, enter NA if you don't care")
    numBe.draw(win)
    numBe.setSize(20)
    numBa = Text(Point(1050,450), "Enter number of bathroom, enter NA if you don't care")
    numBa.draw(win)
    numBa.setSize(20)
    numBed = Text(Point(1050,550), "Enter number of beds, enter NA if you don't care")
    numBed.draw(win)
    numBed.setSize(20)
    
    Pentry = Entry(Point(1100,200),30)
    Pentry.draw(win)
    Sentry = Entry(Point(1100,300),30)
    Sentry.draw(win)
    Beentry = Entry(Point(1100,400),30)
    Beentry.draw(win)
    Baentry = Entry(Point(1100,500),30)
    Baentry.draw(win)
    Bedentry = Entry(Point(1100,600),30)
    Bedentry.draw(win)
    

    confirm = Button(win, 'white', "Confirm", Point(1100,700), 75)

    
'''
    
    while True:
        m1 = win.getMouse()
        if confirm.isClicked(m1):
            error.undraw()
            error2.undraw()
            empty.undraw()
            roominfo.undraw()
            f = fun.getText()
            f1 = fun1.getText()
            c = 0
            for i in data.keys():
                if f1 == data[i]:
                    error.draw(win)
                    c = 1
                if f == i and f1 != data[i]:
                    error2.draw(win)

            if c == 0:
                data[f] = f1


            roominfo.draw(win)
            print(data)
            fun.setText('')
            fun1.setText('')


        if undo.isClicked(m1):
        
            if len(data) != 0:
                data.popitem()
                print(data)
            else:
                empty.draw(win)
            roominfo.draw(win)

'''    
                        
            
                
                
    

if __name__ == "__main__":
    main()
