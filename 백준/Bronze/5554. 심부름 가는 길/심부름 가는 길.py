import sys

Tdistance=[]
for i in range(4):
    Ttime=int(sys.stdin.readline())
    Tdistance.append(Ttime)
total=sum(Tdistance)
print(f"{total//60} {total%60}")