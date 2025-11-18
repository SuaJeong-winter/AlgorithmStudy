def solution(rsp):
    answer = ''
    win={'2':'0','0':'5','5':'2'}
    for case in rsp:
        answer+=win[case]
    return answer