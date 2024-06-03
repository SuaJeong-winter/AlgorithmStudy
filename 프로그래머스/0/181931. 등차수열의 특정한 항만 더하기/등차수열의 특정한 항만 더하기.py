def solution(a, d, included):
    answer = 0
    for num in range(1,len(included)+1):
        if included[num-1]==1:
            value=a+(num-1)*d
            answer+=value
        else:
            pass
    return answer
