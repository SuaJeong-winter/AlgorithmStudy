#같은 원소의 개수를 return하기

def solution(s1, s2):
    answer = 0
    for alpha1 in s1:
        for alpha2 in s2:
            if alpha1==alpha2:
                answer+=1
    return answer


