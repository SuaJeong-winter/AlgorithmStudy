#num을 이루는 숫자 중에 k가 있으면 위치, dkslaus -1을 return

def solution(num, k):
    answer = -1
    num_list = str(num)
    k=str(k)
    if k in num_list:
        answer=str(num).index(k)+1
    return answer