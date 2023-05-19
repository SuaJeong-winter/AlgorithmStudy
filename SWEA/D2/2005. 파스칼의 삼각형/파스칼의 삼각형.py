T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    arr=[[0]*(n+1) for _ in range(n+1)] #패딩포함해서 0으로 초기화
    arr[1][1]=1 #초기값
    for i in range(2, n+1): #i=1은 윗줄에서 이미 초기화를 함
        for j in range(1,i+1):
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
    print(f"#{test_case}")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(arr[i][j], end=" ")
        print()

    # ///////////////////////////////////////////////////////////////////////////////////
