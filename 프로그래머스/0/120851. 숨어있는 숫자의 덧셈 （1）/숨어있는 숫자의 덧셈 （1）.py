def solution(my_string):
    answer = 0
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    for num in my_string:
        if num in num_list:
            answer+=int(num)
    return answer