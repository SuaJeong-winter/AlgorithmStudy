T = int(input()) #테스트케이스
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    p, q, r, s, w = map(int, input().split())  
    coma=w*p 
    comb=0
    if w<r:
        comb=q
    else:
        comb=q+s*(w-r)
    
    result=min(coma, comb)
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
