if __name__ == '__main__':
    n = int(input())
    my_dic = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        my_dic[name] = scores
    query_name = input()
    # create new list with the new query name
    new_list = list(my_dic[query_name])
    average = sum(new_list)/len(new_list)
    # adding two decimal places in the average
    print('%.2f'% average)