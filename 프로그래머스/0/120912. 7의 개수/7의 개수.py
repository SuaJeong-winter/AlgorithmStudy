def solution(array):
    answer = 0
    str_ans=""
    for num in array:
        str_ans += str(num)
    answer = str_ans.count('7')
    return answer