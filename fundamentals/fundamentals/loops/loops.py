for x in range(0,10, 3): #first value = start, second: maxValue, third: amount it can increase
    print(x)
#Looping Over Lists & Strings
for x in "Hello": # output: 'H', 'e', 'l', 'l', 'o'
    print(x)

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

#While Loops
for count in range(0,5):
    print("looping = ", count)
#rewrite using while loop
count= 0
while count <=5:
    print("looping -", count)
    count+=1

#For Loops through Dictionaries:When we iterate through a dictionary, the iterator is each of the keys of the dictionary.

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(each_key)
# output: name, language

#That means if we want the values of our dictionary, we might do something like this:
my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python
#Dictionaries also have a few additional methods that allow us to iterate through them and have the keys and/or values as the iterator. Test these out to get a better understanding:
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc
#The provided code stub reads an integer, n, from STDIN. For all non-negative integers i<n , print i*i.
n = int(input())
for i in range(0,n):
    print(i*i)
