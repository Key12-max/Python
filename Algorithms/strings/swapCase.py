def swap_case(s):
    k= ''
    for i in s:
        if i.upper() != i:
            k+=i.upper()
        elif i.lower() !=i:
            k+=i.lower()
        else:
            k+=i
    return k

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)