def solution(num_list):
    answer = []
    for num in range(len(num_list)-1,-1,-1):
        answer.append(num_list[num])
    return answer