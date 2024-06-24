def solution(intStrs, k, s, l):
    answer = []
    number=0
    for word in intStrs:
        number=int(word[s:s+l])
        if number>k:
            answer.append(number)
    return answer
