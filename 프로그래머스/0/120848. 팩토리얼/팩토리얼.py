def solution(n):
    answer = 0
    mul_sum=1
    while(1):
        mul_sum*=(answer+1)
        if mul_sum<=n:
            answer+=1
        else:
            return answer

