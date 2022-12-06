import random
import time
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
    start = time.time()
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
            if L[i]>L[i+1]:
                isSorted = False
        if isSorted:
            break
    stop = time.time()
    total = stop - start
    print(total)
            


if __name__ == "__main__":
    main()
