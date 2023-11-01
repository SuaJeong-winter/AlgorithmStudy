import sys

num=int(sys.stdin.readline().rstrip())
result=0
for i in range(1,num+1):
    result+=i
print(result)