def solution(my_string, n):
    answer = ''
    for alpha in my_string:
        answer+=alpha*n
    return answer