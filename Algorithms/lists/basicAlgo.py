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
print("===Determin the max of two number===")
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

print("===check if element exists in lis in Python===")
def is_elementExists(arrList, toBechecked):
    count = 0
    if toBechecked in arrList:
        count += 1
        print(f"It exists  {count}  times")
    else:
        print("does not exist")
test_list = [1, 6, 3, 5, 3, 4]
test_value = 3
is_elementExists(test_list,test_value)

print("====different way clear a list===")
#using the clear method
Geek = [6, 0, 4, 1]
Geek.clear()
print('Geek after clear:', Geek)
#using Reinitializing
list1 = [1,3,5,6]
#deleting list using reinitialization
list1 = []
print("List1 after clearing using reinitialization: " + str(list1))

print("===reversing a list ===")
#using slicing technique which returns a new list from existing list.
def Reverse(lst):
    new_lst = lst[::-1] #this indicates where to start, where to end, and specify the step.
    #lst[Initial: End: IndexJump ] this the format for slicing in python
    return new_lst
lst = [10, 11, 12, 13,14, 15]
print(Reverse(lst))
# Reverse list by swapping present and last numbers at a time
def list_reverse(arr, size):
    #if only one element present , then retrun the array
    if(size==1):
        return arr
    #if only two elements present, then swap first and last numbers.
    elif(size==2):
        arr[0],arr[1] = arr[0], arr[1]
        return arr
    #if more than two element presents, then swap first and last number
    else:
        i = 0
        while(i<size//2):
            #swap present and preceding numbers at time and jump to second element after swap
            arr[i], arr[size-i-1] = arr[size-i-1], arr[i]
            #skip if present and preceding numbers indexes are same
            if((i!=i+1 and size-i-1 != size-i-2) and (i != size-i-2 and size-i-1!=i+1)):
                arr[i+1], arr[size-i-2] = arr[size-i-2], arr[i+1]
            i+=2
        return arr
arr = [1,2,3,4,5]
size = 5
print("Original list:", arr)
print("Reversed list: ", list_reverse(arr, size))

print("===Reverse a list using a two-pointer approac===")
def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left<right):
        #swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr
arr = [1,2,3,4,5,6,7]
print(reverse_list(arr))

print("===ways to remove particular list element===")
test_list1 = [1,3,4,6,3]
test_list2 = [1,4,5,4,5]
# using remove() to remove list element3
# only first occurance deleted
test_list1.remove(3)
print("the list after element removal is : " + str(test_list1))

#using list comprehension
# to remove list element 4
test_list2 = [x for x in test_list2 if x != 4]
print("The list after element removal is : " + str(test_list2))

print("===Remove multiple element===")
list1 = [11, 5, 17, 18, 23, 50]
for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)
print("New list after removing all even numbers: ", list1)

#using comprehension
list1 = [ elem for elem in list1 if elem % 2 != 0]
print(*list1)

print("===concatenate every elements across lists ===")
test_list1 = [[4,3,5,],[1,2,3],[3,7,4]]
test_list2 = [[1,3],[9,3,5,7],[8]]

for i in range(0, len(test_list1)):
    test_list1[i].extend(test_list2[i])
print("The concatenated Matrix: " + str(test_list1))
#element repetiton in list
test_list = [4, 5, 6, 3, 9]
res = [i for i in test_list for x in (0,1)]
print("The list after elemenet duplication " + str(res))
#Repeat alternate elements in a list
test_list = [4,5,6]
k= 3
res = []
for i in range(0, len(test_list)):
    if(i%2 == 0):
        res.extend([test_list[i]]*k)
print("The list after alternate repeating elements : " + str(res))

print("===Deffirence between two list(list1-list2) ===")
list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]
temp3 = []
for elemenet in list1:
    if elemenet not in list2:
        temp3.append(elemenet)
print(temp3)

print("===Check if two lists are identical===")
test_list1 = [1,2,3,4,5]
test_list2 = [1,2,4,3,5]
test_list1.sort()
test_list2.sort()
if test_list1 == test_list2:
    print("The lists are identical ")
else:
    print("The lists are not identical")

print("===combining two sorted lists===")
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
size_1 = len(test_list1)
print(size_1)
size_2 = len(test_list2)
print(size_2)
res = []
i,j = 0,0
while i<size_1 and j<size_2:
    if test_list1[i] < test_list2[j]:
        res.append(test_list1[i])
        i += 1
    else:
        res.append(test_list2[j])
        j += 1
res = res + test_list1[i:] + test_list2[j:]
print("The combined sorted list is: " + str(res))
print("====copy or clone a list using slcicing technique===")
def Cloning(lil):
    li_copy = lil[:]
    return li_copy
lil = [4, 8, 2, 10, 15,18]
li2 = Cloning(lil)
print("Original List: ", lil)
print("After Cloning: ", li2)

#python3 code to iterate over a list
list = [1, 3, 5, 7, 9]
#using enumerate()
for i, val in enumerate(list):
    print(i, ", ", val)

#iterate over list using while loop.
i = 0
while i<len(list):
    print(list[i])
    i +=1
#list comprehension
#snytax newList = [expression(element) for element in oldList if condition]
numbers = [12, 13, 14]
double = [x*2 for x in numbers]
print(double)

# even list using list comprehension

list = [i for i in range(11) if i% 2 ==0]
print(list)

#matrix using list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

#list comprehensions vs for loop
list = []
for character in 'Geeks 4 Geeks!':
    list.append(character)
print(list)

list = [character for character in 'Geeks 4 Geeks!']
print(list)

print("====Concatenate two list of list===")
input_list1 = [[4,3,5],[1,2,3],[3,7,4]]
input_list2 = [[1,3], [9,3,5,7],[8]]
for i in range(0, len(input_list1)):
    # extend method in python is used for extending lists by adding all the elements of the iterable at the end of privious list
    input_list1[i].extend(input_list2[i])
print("The concatenated Matix: " + str(input_list1))

print("===check if two list are identical==")

input_list1.sort()
input_list2.sort()
if input_list1 == input_list2:
    print("The list are identical")
else:
    print("This lists are not identical")