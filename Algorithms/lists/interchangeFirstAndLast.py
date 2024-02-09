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

print("===Swap two elements in a list===")
#swap functions
def swapPositions(list, pos1,pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
#driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1,3
print(swapPositions(List, pos1-1, pos2-1))

#or
def swapPositions(lis, pos1, pos2):
    temp = lis[pos1]
    lis[pos1] = lis[pos2]
    lis[pos2] = temp
    return lis
#driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1-1, pos2-1))

print("===Determin length of lists with out using len method==")
#initialize list
test_list = [1, 4, 5, 7, 8]
#finding length of list using loop
#initializing counter
counter = 0
for i in test_list:
    #increment counter
    counter +=1
print("Length of list using native method is : " + str(counter))

def maxTwoNumber(a, b):
    if a>b:
        max = a
        print(max)
    else:
        max = b
        print(max)
maxTwoNumber(-2,-4)
# use  of ternary operator
a,b = 2,8
# Copy value of a in max if a>b else copy b
max  = a if a>=b else b
print(max)
