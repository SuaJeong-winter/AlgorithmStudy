T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num= int(input())
    a,b,c,d,e = 0,0,0,0,0
    while num!=1:
        if num %2==0:
            num=num//2
            a+=1
        elif num%3==0:
            num=num//3
            b+=1
        elif num%5==0:
            num=num//5
            c+=1
        elif num%7 ==0:
            num=num//7
            d+=1
        elif num%11==0:
            num=num//11
            e+=1
        else:
            pass
    print(f"#{test_case} {a} {b} {c} {d} {e}")
    # ///////////////////////////////////////////////////////////////////////////////////
