def solution(my_string):
    w_list=[]
    for i in range(len(my_string)):
        w_list.append(my_string[i:])
        w_list.sort()
    return w_list