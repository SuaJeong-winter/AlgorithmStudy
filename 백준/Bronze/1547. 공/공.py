import sys

m=int(sys.stdin.readline())
cup=[1,2,3]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    store=cup[a-1]
    cup[a-1]=cup[b-1]
    cup[b-1]=store

print(cup.index(1)+1)
