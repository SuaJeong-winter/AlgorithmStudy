import sys

for _ in range(3):
    n=int(sys.stdin.readline())
    sum=0
    for _ in range(n):
        num=int(sys.stdin.readline())
        sum+=num
    if sum==0:
        print("0")
    elif sum>0:
        print("+")
    else:
        print("-")