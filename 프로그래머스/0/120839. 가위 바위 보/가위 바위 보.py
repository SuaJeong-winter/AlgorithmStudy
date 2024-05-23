def solution(rsp):
    answer = ''
    winning = {'2':'0','0':'5','5':'2'}
    for case in rsp:
        answer+="".join(winning[case])
    return answer