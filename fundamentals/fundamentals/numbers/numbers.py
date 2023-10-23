#Conversion
int_to_float = float(35)
float_to_int = int(35.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

#Random number: python does not have a built in random number generator, instead use random module
import random
print(random.randint(2,7))
