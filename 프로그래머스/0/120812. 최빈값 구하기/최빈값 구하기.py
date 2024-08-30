def solution(array):
    cnt_arr=[0]*1000
    result=0
    for num in array:
        cnt_arr[num]+=1
    max_num=max(cnt_arr)
    for maxvalue in cnt_arr:
        if maxvalue == max_num:
            result+=1
    if result != 1:
        return -1
    else:
        return cnt_arr.index(max_num)