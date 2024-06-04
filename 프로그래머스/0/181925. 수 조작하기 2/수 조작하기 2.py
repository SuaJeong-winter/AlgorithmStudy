def solution(numLog):
    answer = ''
    for i in range(1,len(numLog)):
        gap = numLog[i]-numLog[i-1]
        if gap ==1:
            answer+="".join("w")
        elif gap ==-1:
            answer+="".join("s")
        elif gap == 10:
            answer+="".join("d")
        elif gap ==-10:
            answer+="".join("a")
    return answer
