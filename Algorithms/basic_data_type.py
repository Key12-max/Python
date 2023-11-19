"""
Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.
"""
N = int(input())
mylist = []
for i in range(N):
    s = list(input().split())
    if s[0] == "append":
        mylist.append(int(s[1]))
    if s[0]=='remove':
        mylist.remove(int(s[1]))
    s = list(input().split())
    if s[0]=='insert':
        mylist.insert(int(s[1]), int(s[2]))
    if s[0]=='sort':
        mylist.sort()
    if s[0]=='pop':
        mylist.pop()
    if s[0]=='reverse':
        mylist.reverse()
    if s[0]=='print':
        print(mylist)