#n이 제곱수라면 1 아니라면 2를 return

def solution(n):
    answer = 2
    for num in range(1,n//2+1):
        if num*num==n:
            answer=1
        else:
            pass

    return answer