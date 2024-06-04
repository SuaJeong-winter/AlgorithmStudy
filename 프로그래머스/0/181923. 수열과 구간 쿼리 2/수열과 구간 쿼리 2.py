def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        value=[]
        for idx in range(len(arr)):
            if s<=idx<=e and arr[idx]>k:
                value.append(arr[idx])
        if len(value)==0:
            value.append(-1)
        answer.append(min(value))
    return answer