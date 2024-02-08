"""
Create a function sum() that returns the sum of the two numbers passed as its arguments.

For example, sum(2,5) should return 7; sum(3,10) should return 13.
"""
def sum(num1, num2):
    print(num1+num2)

sum(2,5)

""" countdown by 8"""
def countDown8(i):
    k=2019
    while k>1900:
        k=k-i
        print(k)
countDown8(8)
"""
Kelvin wants to convert between temperature scales. Create celciusToFahrenheit(cDegrees) that accepts a number of degrees in Celcius, and returns the equivalent temperature as expressed in Fahrenheit degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.
"""
def celciusToFahrenheit(cDegrees):
    fahrenheit = (9/5*cDegrees)+32
    print(fahrenheit)
celciusToFahrenheit(8)

"""Given an array, write a function that changes all positive numbers in the array to “big”.

Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,"big","big",-5]."""
def makeItBig(arr):
    for i in range(len(arr)):
        if arr[i]>=0:
            arr[i]=str("big")
            print(arr)
makeItBig([-4,3,5,-5])

"""
Given an array, create a function to return a new array where each value in the original has been doubled. Calling double([1,2,3]) should return [2,4,6].
"""
def double(arr2):
    for i in range(len(arr2)):
        result = arr2[i]*2
        print(result)
double([1,2,3])

"""
Given an array and a value Y, count and return the number of array values greater than Y.

For example, returnArrayCountGreaterThanY( [2,3,5], 4) should return 1 as there is only one element in the array whose value is greater than 4.
"""
def  returnArrayCountGreaterThanY(arr, y):
    count = 0
    for i in range(len(arr)):
        if arr[i]>y:
            count=count+1
            print(count)
returnArrayCountGreaterThanY([2,3,5],4)

"""
Just the Facts, ma’am. Factorials, that is. Write a function factorial(num) that, given a number, returns the product (multiplication) of all positive integers from 1 up to number (inclusive).

For example, factorial(3)=6(or1 * 2 * 3);factorial(5)=120(or1 * 2 * 3 * 4 * 5).
"""

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact=fact*i
        print(fact)
factorial(5)


"""
Create threesFives(n) that adds values from 1 and n (inclusive) if that value is not divisible by 3 or 5. Return the final sum.

For example, threesFives(10) returns 22 as it only returns the sum of 1, 2, 4, 7, and 8. In that example, it skips 3, 6, and 9 as those are divisible by 3. It also skips 5, and 10 as it's divisible by 5.

"""
def threeFives(n):
    sum = 1
    for i in range(n):
        if n%5 !=0 or n%3!=0:
            sum = sum+i
            print(sum)
threeFives(10)

"""
Create a function that prints/logs all the integers from 1 to 20.
"""
def print1to20():
    for i in range(1,21):
        print(i)
print1to20()

"""Create a function that prints/logs all the odd numbers from 3 to 20."""
print("=====print the odd numbers between 3 and 20==========")
def printOdd3to20():
    for i in range(3,20):
        if i%2!=0:
            print(i)
printOdd3to20()


print("===Print/log all the multiples of 7 between the numbers 7 to 62.===")
def multipleOf7():
    for i in range(7,62):
        if i%7==0:
            print(i)
multipleOf7()

print("===Log positive numbers starting at 50, counting down by fives (exclude 0).===")
def logPositiveNumbersCountingDownBy5():
    for i in range(50,0,-5):
        if i>0:
            print(i)
logPositiveNumbersCountingDownBy5()

print("===Given an array, print/log the sum of the first value in the array, plus the array’s length. Assume that the array is composed of numbers.===")
def firstPlusLength(arr):
    sum = 0
    for i in range(len(arr)):
        sum = arr[i]+len(arr)
        print(sum)
firstPlusLength([1,5,7,9,13])

print("===Remove duplicate array from sorted array===")
#not quite solved yet.
def removeDuplicates(nums,n):
    #return, if array is empty or containws a single element
    if n == 0 or n == 1:
        return n
    temp = list(range(n))
    #start traversing elements
    count = 0
    for i in range(0, n-1):
        if nums[i]!= nums[i+1]:
            temp[count] = nums[i]
            count += 1
    #store the last element as whether it is unique or repeated, it is not stored previously
    temp[count] = nums[n-1]
    count += 1
    #modify the original array
    for i in range(0,count):
            nums[i] = temp[i]
            #print(nums[i])
    return count
if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    n = len(nums)
    #removeDuplicates() returns new size of array
    n = removeDuplicates(nums,n)
    for i in range(n):
        print("%d" % (nums[i]), end=" ")

#removeDuplicates([],5)


