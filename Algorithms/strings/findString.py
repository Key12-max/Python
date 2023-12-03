"""
the function count_substing initializes a variable count to 0
and enters a while loop that continues as long as the substring appears 
within string.
within while loop, the code uses string method "find()" to locate
the first occurance of substring with in the sting, assings the index of 
this occurance to the variable "a", then re-assings the string to a slice that starts
one character after the end of the substring. finally,it increases the count by 1. 
when the substring is no longer in the string, the function returns the final count of the substring occurances.


"""

def count_substring(string, sub_string):
    count = 0
    while sub_string in string:
        a = string.find(sub_string)
        string = string[a+1:]
        count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)