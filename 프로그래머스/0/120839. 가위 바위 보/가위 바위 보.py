def solution(rsp):
    answer = ''
    win_rule={'2':'0','0':'5','5':'2'}
    for utry in rsp:
        answer+= ''.join(win_rule[utry])
    return answer