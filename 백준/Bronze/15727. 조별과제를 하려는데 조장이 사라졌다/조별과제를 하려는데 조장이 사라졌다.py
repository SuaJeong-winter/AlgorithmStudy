import sys

distance=int(sys.stdin.readline())
length=5
cnt=0
while(distance!=0):
    if distance//length>=1:
        distance-=length
        cnt+=1
    else:
        length-=1

print(cnt)