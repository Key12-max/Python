#F-Strings (Literal String Interpolation)
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

#string.format()
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

#Built-In String Methods: not only this, but here are some ;
""" 
string.upper(): returns a copy of the string with all the characters in uppercase.
string.lower(): returns a copy of the string with all the characters in lowercase.
string.count(substring): returns number of occurrences of substring in string.
string.split(char): returns a list of values where string is split at the given character.
"""