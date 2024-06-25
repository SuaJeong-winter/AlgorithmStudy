def solution(my_string, is_prefix):
    answer = 0
    w_list=[]
    for idx in range(1,len(my_string)):
        w_list.append(my_string[:idx])
    if is_prefix in w_list:
        answer=1
    return answer