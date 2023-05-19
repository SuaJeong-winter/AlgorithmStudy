T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,k=map(int,input().split())
    wboard=[list(map(int,input().split())) for _ in range(n)]
    cnt=0
    for i in range(n): #행을 검사
        wlen=0
        for j in range(n):
            if wboard[i][j]==1:
                wlen+=1
            if wboard[i][j]==0 or j==n-1:
                if wlen ==k:
                    cnt+=1
                wlen=0
                    
        for j in range(n):  #열을 검사
            if wboard[j][i] ==1:
                wlen+=1
            if wboard[j][i]==0 or j==n-1:
                if wlen==k:
                    cnt+=1
                wlen=0
                
    print(f"#{test_case} {cnt}")   
    # ///////////////////////////////////////////////////////////////////////////////////
