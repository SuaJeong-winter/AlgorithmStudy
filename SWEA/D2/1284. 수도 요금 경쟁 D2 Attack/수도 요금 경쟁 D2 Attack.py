T=int(input())
for t in range(1,T+1):
    p,q,r,s,w=map(int,input().split())
    a_price=p*w
    if w<=r:
        b_price=q
    else:
        b_price=q+(w-r)*s
    print(f"#{t} {min(a_price,b_price)}")
