def solution(n):
    answer=1
    while (1):
        if n>(7*answer):
            answer+=1
        else:
            return answer