T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n=int(input())
    result = [[1] for _ in range(n)]
    
    for i in range(1,n):
        if i==1:
            result[i].append(1)
            continue
        for j in range(1,i):
            result[i].append(result[i-1][j-1]+result[i-1][j])
        result[i].append(1)
        
    for i in result:
        if len(i)==1:
            print("#{}\n{}".format(test_case, *i))
        else:
            print(*i)
        
              
    # ///////////////////////////////////////////////////////////////////////////////////
