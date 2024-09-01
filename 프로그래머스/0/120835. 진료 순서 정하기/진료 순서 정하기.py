def solution(emergency):
    answer = [0]*len(emergency)
    num=1
    e_arr= sorted(emergency,reverse=True)
    for order in e_arr:
        answer[emergency.index(order)]=num
        num+=1

    return answer