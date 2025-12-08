#문자열 my_str을 길이 n씩 잘라서 저장하기

def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i + n])
    return answer

