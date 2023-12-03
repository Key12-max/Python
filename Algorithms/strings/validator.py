"""
Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""
if __name__ == '__main__':
    s = input()
    res = False
    for i in s:
        if i.isalnum():
            res = True
            break
    print(res)

    res = False
    for j in s:
        if j.isalpha():
            res = True
            break
    print(res)

    res = False
    for k in s:
        if k.isdigit():
            res = True
            break
    print(res)

    res = False
    for g in s:
        if g.islower():
            res = True
            break
    print(res)

    res = False
    for m in s:
        if m.isupper():
            res = True
            break
    print(res)