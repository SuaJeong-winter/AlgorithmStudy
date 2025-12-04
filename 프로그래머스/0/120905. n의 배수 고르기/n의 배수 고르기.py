#num_list에서 n의 배수가 아닌 수들을 제거해서 출력

def solution(n, numlist):
    answer = []
    for number in numlist:
        if number%n==0:
            answer.append(number)
    return answer