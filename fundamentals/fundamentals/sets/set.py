"""
Task

Apply your knowledge of the .add() operation to help your friend Rupal.

Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps.

Input Format

The first line contains an integer , the total number of country stamps.
The next  lines contains the name of the country where the stamp is from.
Constraints


Output Format

Output the total number of distinct country stamps on a single line.

Sample Input

7
UK
China
USA
France
New Zealand
UK
France 
Sample Output

5
Explanation

UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).
"""


"""N = int(input())
mySet = ()
for i in range(N):
    mySet.__add__(input)
print(len(mySet))"""
#you can test it on your terminal

"""COMMON SET OPERATIONS Using union(), intersection() and difference() functions."""
myset = set([])
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
a.union(b) # Values which exist in a or b
{2, 4, 5, 9, 11, 12}
a.intersection(b) # Values which exist in a and b
{2, 4}
a.difference(b) # Values which exist in a but not in b
{9, 5}

