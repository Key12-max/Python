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
    