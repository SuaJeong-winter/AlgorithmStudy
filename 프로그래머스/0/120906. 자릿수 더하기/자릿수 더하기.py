#n의 각 자리의 숫자 합을 return

def solution(n):
    answer = 0
    str_n = str(n)
    for number in str_n:
        answer+=int(number)
    return answer
