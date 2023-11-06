import sys

a,b,c=list(map(int,sys.stdin.readline().split()))
result=sorted([a,b,c])
for i in range(3):
    print(result[i],end=" ")
