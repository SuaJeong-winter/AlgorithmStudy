def solution(my_string, n):
    answer = ''
    for alpha in my_string:
        answer+="".join(alpha*n)
    return answer