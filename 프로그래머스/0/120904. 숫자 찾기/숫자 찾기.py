#num을 이루는 숫자 중에 k가 있으면 위치, dkslaus -1을 return

def solution(num, k):
    answer = -1
    num_list = str(num)
    for number in num_list:
        if number == str(k):
            answer = num_list.index(number) + 1

    return answer