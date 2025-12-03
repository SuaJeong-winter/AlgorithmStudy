#주어진 숫자의 약수를 오름차순으로 구하시오

def solution(n):
    answer = []
    for i in range(1,n+1):
        if n%i==0:
            answer.append(i)
    return answer