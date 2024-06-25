def solution(my_string, is_suffix):
    answer = 0
    w_list=[]
    for idx in range(len(my_string)):
        w_list.append(my_string[idx:])
    if is_suffix in w_list:
        answer=1
    return answer