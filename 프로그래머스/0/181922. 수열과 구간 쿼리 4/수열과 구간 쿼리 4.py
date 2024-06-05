def solution(arr, queries):
    for s,e,k in queries:
        for idx in range(len(arr)):
            if s<=idx<=e and idx%k==0:
                arr[idx]+=1

    return arr