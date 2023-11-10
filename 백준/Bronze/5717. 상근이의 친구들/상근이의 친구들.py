import sys

while(1):
    m, f = map(int, sys.stdin.readline().split())
    if m==0 and f==0:
        break
    else:
        print(m+f)