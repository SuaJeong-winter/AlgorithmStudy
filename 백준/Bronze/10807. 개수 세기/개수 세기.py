import sys  

n=int(input())
a=list(map(int,sys.stdin.readline().split()))
v=int(input())
countv=0
for i in range(n):
  if (a[i]==v):
    countv+=1
  else:
    pass
print(countv)