def solution(array):
    answer = 0
    ans_arr=[0]*1000
    for num in array:
        ans_arr[num]+=1
    max_num= max(ans_arr)
    if ans_arr.count(max_num)==1:
        answer = ans_arr.index(max_num)
    else:
        answer= -1

    return answer