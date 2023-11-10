import sys

num=int(sys.stdin.readline())
cars=list(map(int,sys.stdin.readline().split()))
cnt=0

for i in range(len(cars)):
    if cars[i]==num:
        cnt+=1

print(cnt)

