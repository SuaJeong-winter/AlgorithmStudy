def solution(my_string, index_list):
    answer = ''
    for idx in index_list:
        answer+="".join(my_string[idx])
    return answer