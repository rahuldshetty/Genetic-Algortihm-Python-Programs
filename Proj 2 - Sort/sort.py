import random
from datetime import datetime
random.seed()

startTime = datetime.now()

def fitness(arr):
    s=0
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:s+=1
    return s

def mutate(arr):
    id1 = random.randrange(0,len(arr))
    id2 = random.randrange(0,len(arr))
    prevFitness = fitness(arr)
    tmp = arr
    tmp[id1],tmp[id2] = tmp[id2],tmp[id1]
    newFitness = fitness(tmp)
    if newFitness >= prevFitness:
        return tmp
    else :return arr 

def display(guess,fit):
    time = datetime.now() - startTime
    print("{}\t{}\t{}".format(guess,time,fit))



def main():
    arr = [int(x) for x in input('Enter numbers:').split()]

    bestScore = fitness(arr)
    display(arr,bestScore)

    while True:
        newArr = mutate(arr)
        fit = fitness(newArr)

        if fit == len(newArr)-1:
            arr = newArr
            bestScore = fit
            break
        else:
            if fit >= bestScore:
                bestScore = fit
                arr = newArr
            
            display(arr,bestScore)

            continue
    
    print("Sorted Array:",arr,bestScore)

if __name__ == "__main__":
    main()