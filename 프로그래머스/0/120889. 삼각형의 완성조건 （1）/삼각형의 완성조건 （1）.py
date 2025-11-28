def solution(sides):
    answer = 0
    s_len=[]
    s_len=sorted(sides)
    if s_len[-1]<(s_len[0]+s_len[1]):
        answer=1
    else:
        answer=2
    return answer