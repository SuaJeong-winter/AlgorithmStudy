T=int(input())
cal = {1:31,2:28,3:31, 4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for test_case in range(1,T+1):
    m1,d1,m2,d2=map(int,input().split())
    lday1,lday2=0,0
    for i in range(1,m1):
        lday1+=cal[i]
    lday1+=d1
    for j in range(1,m2):
        lday2+=cal[j]
    lday2+=d2
    print(f"#{test_case} {lday2-lday1+1}")
