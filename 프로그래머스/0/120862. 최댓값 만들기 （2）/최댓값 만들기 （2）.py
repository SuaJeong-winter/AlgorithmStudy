#배열 numbers의 두 수를 곱해서 만들 수 있는 최댓값을 return

def solution(numbers):
    s_numbers=sorted(numbers)
    answer=s_numbers[0]*s_numbers[1]
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            std=s_numbers[i]*s_numbers[j]
            if std>answer:
                answer=std
    return answer