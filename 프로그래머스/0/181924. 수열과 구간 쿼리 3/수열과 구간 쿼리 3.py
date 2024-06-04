def solution(arr, queries):
    for i in range(len(queries)):
        box=arr[queries[i][0]]
        arr[queries[i][0]]=arr[queries[i][1]]
        arr[queries[i][1]]=box
    return arr