import random
def main():


    L = [32,14,4,90]

    print(L)
    '''
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j]>L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
            print(L)
    '''

    G = L
    maxPos = len(L)-2
    
    while True:
        randomPos1 = random.randint(0,maxPos)
        randomPos2 = random.randint(0,maxPos)
        temp = L[randomPos1]
        L[randomPos1] = L[randomPos2]
        L[randomPos2] = temp 
        print(L)
        
        isSorted = True
        for i in range(len(L)-1):
            if G[i]>G[i+1]:
                isSorted = False
        if isSorted:
            break
            


if __name__ == "__main__":
    main()
