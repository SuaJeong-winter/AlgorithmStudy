import math

def solution(n):
    answer = 0
    for num in range(1,n+1):
        cnt=0
        for val in range(1,num+1):
            if num%val==0:
                cnt+=1
        if cnt>2:
            answer+=1
    return answer
