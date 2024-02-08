#Python3 program to swap first and last element of list

#swap function
def swapList(newList):
    #determin size or length of list
    size = len(newList)

    #swapping 
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp
    
    return newList
#Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#second method

def swapList(newList):
    #last element of list can be referred as list[-1].
    #So, we can simply swap list[0] with list[-1]
    newList[0],newList[-1] = newList[-1],newList[0]
    
    return newList
#Driver code
newList = [12,35, 9, 56, 24]
print(swapList(newList))