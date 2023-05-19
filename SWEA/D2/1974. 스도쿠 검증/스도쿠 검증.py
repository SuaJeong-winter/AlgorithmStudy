T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    gboard=[list(map(int,input().split())) for _  in range(9)]
    result=1 #기본값은 true
    for i in range(9):
        cnt_r = [0]*10
        cnt_c = [0]*10
        for j in range(9):
            cnt_r[gboard[i][j]]+=1
            cnt_c[gboard[j][i]] +=1
            
        for k in range(1,10):
            if cnt_r[k]!=1:
                result=0
                break
            if cnt_c[k] !=1:
                result=0
                break
          
    for i in range(3):
        for j in range(3):
            cnt_x=[0]*10
            for k in range(3):
                for l in range(3):
                    cnt_x[gboard[3*i+k][3*j+l]]+=1
            
            for k in range(1,10):
                if cnt_x[k] !=1:
                    result=0
                    break
            
           
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
