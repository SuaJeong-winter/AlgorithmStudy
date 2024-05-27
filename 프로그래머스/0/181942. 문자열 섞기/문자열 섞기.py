def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += "".join(str1[i])
        answer += "".join(str2[i])
    return answer