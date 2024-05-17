def solution(num_list):
    answer = [0,0]
    cnt_odd, cnt_even = 0,0
    for index in num_list:
        if index%2 ==0:
            cnt_even+=1
        else:
            cnt_odd+=1
    answer[0],answer[1] = cnt_even,cnt_odd

    return answer