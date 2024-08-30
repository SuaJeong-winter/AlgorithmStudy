def solution(array):
    # 배열을 정렬
    arr=sorted(array)
    # 배열의 중앙값 찾기
    answer=arr[len(array)//2]

    return answer