# Map function in python has this syntax map(func, *iterables)
# it returns a map object which is a generator object
# the number of arguments to func must be the number of iterables listed
# Say, I have a list(iterable) of my favorite pet names, 
# all in lower case and I need them in uppercase. 
my_pets = ["alfred", "tabitha", "william","arla"]
uppered_pets = []
for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)
print(uppered_pets)

# With map() function
uppered_pets = list(map(str.upper,my_pets))
print(uppered_pets)
#note we did not call the str.upper as str.upper(), as 
# the map function does that for us on each element in the my_pets list.
