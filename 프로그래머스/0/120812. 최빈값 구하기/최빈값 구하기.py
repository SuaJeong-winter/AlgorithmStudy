def solution(array):
    num_arr = [0]*(max(array)+1)
    max_cnt=0
    for i in array:
        num_arr[i]+=1

    for j in num_arr:
        if j == max(num_arr):
            max_cnt +=1

    if max_cnt > 1:
        return -1
    else:
        return num_arr.index(max(num_arr))