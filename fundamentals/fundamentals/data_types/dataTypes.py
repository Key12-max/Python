#Primitive data types
    #booolean values
is_hungry = True
has_feckles = False
    #Numbers
age = 14 #int
weight = 150.34 #float
    #STring
name = "kiros"
#Composit types: Tuples, List, Dictionary

dog = ("Bruce", "Cocker spaniel", 16, False)
print(dog[0])
#can not modifed

heros = ['Rozen', 'KB', 'Oliver', 'merry'] #mutable and containes similar data type only unlike tuple
print(heros[2])
heros[0] = 'Francis'
heros.append('Mikeal')
print(heros)
heros.pop()
print(heros)	# output: ['Francis', 'KB', 'Oliver']
heros.pop(1)
print(heros)	# output: ['Francis', 'Oliver']
#It's also useful to know that Python uses the following syntax: [:] to return a copy of some portion of the list, constrained by specified indices. This is called slicing.
print(heros[1:])
print(heros[:2])
print(heros[1:2])


#Dictionary
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}    

#Common functions: use "type" function to identify the varialble or value data type
print(type(2.65)) #output float
print(type(new_person)) #output dict
