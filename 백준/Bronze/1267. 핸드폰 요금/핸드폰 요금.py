import sys

call=int(sys.stdin.readline())
phoneTime=list(map(int,sys.stdin.readline().split()))
sumY=0
sumM=0
for i in range(len(phoneTime)):
    Yprice = ((phoneTime[i]//30+1)*10)
    Mprice = ((phoneTime[i]//60+1)*15)
    sumY+=Yprice
    sumM+=Mprice
if sumY==sumM:
    print(f"Y M {sumY}")
elif sumY>sumM:
    print(f"M {sumM}")
else:
    print(f"Y {sumY}")
