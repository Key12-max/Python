#The def keyword signifies the declaration of a function.
def say_hi(name):
    print("Hi, " + name)
say_hi("kiros")
say_hi("merry")
#Returning Values: inorder to use the value later in our progaram
#t is very important to remember this: a function call is equal to whatever that function returns.
def say_hi(name):
    return "Hi " + name
greeting = say_hi("Mickeal")
print(greeting)