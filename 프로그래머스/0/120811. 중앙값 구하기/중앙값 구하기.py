def solution(array):
    answer = 0
    sort_arr = sorted(array)
    mid_index=len(array)//2
    answer = sort_arr[mid_index]
    return answer

