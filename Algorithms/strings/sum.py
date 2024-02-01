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
    for i in arr:
        if i <0:
            arr[i]="big"
            print(arr)
makeItBig([-1,3,5,-5])