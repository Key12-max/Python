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
        if arr[i]<=-1:
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