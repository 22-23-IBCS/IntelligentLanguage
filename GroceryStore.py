class Grocery:
    def __init__(self, dic, name, manager):
        self.d = dic
        self.n = name
        self.m = manager
        
    def getList(self):
        return list(self.d.keys())
    
    def purchase(self,l):
        money = 0
        for i in l:
            money = money + int(self.d.get(i) )
        return money
    def speaking(self):
        return self.m + ": \"Welcome to my store. Luckily you are the first costumer who talk with me. You can get everything free from here!\""
            
        
        

def main():
    ggg = {"pizza" : 10,
          "Sandwich" : 11,
          "chicken wings" : 5,
          "pasta" : 7,
          "ice cream" : 8,
          "boba tea" : 3,
          "cocacola" : 5,
          "sprite" : 1,
          "water" : 1,
          "kit-kat" : 0.5}
    store = Grocery(ggg, "Charles's random store", "Charles")
    
    print(store.getList())
    toBuy = []
    while True:
        res = input("What would you like to buy? Enter 'stop' if done\n")
        if res == 'stop':
            break
        else:
            toBuy.append(res)
    print(toBuy)
    print("Your total prices are: $" + str(store.purchase(toBuy)))
    print(store.speaking())
    
    


if __name__ == "__main__":
    main()
