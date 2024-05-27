def solution(n):
    answer = 0
    if n%2 !=0:
        for cnt in range(1,n+1):
            if cnt%2 !=0:
                answer+=cnt
        return answer
    else:
        for cnt in range(1,n+1):
            if cnt%2==0:
                answer+=cnt**2
        return answer