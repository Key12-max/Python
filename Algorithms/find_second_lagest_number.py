# Find the Second Largest Number

# You are given N numbers. Store them in a list and find the second largest number.

# Input Format 
# The first line contains N. The second line contains an array A[] of N integers each separated by a space.

# Constraints
# 2 <= N <= 10
# -100 <= A[i] <= 100

# Output Format 
# Output the value of the second largest number.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # new_list is a set of list1 which is arr
    new_list = set(arr)

# Removing the largest element from temp list
    new_list.remove(max(new_list))
    
    print(max(new_list))

