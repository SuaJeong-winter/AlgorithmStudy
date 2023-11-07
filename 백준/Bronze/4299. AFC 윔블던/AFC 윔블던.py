import sys

sum,sub= map(int,sys.stdin.readline().split())

if (sum-sub)%2!=0 or sum-sub<0:
    print(-1)
else:
    a=(sum+sub)//2
    b=(sum-sub)//2
    print(a,b)
