#array의 원소들 중 매개변수 n과 가장 가까이에 있는 수는?

def solution(array, n):
    answer = 0
    array=sorted(array,reverse=True)
    min_num=100
    for num in array:
        if min_num>=abs(n-num):
            min_num=abs(n-num)
            answer=num

    return answer
