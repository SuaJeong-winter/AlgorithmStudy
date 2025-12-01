#문자열에 있는 숫자를 차례대로 더 하지만
#Z가 나오면 이전에 더했던 값을 뺀다

def solution(s):
    answer=0
    s_group = s.split()
    sum_group = []
    for val in s_group:
        if val == "Z":
            sum_group.pop()
        else:
            sum_group.append(int(val))
    answer = sum(sum_group)
    return answer
