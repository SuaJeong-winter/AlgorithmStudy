import sys

n,m,k=map(int,sys.stdin.readline().split())
print(f"{k//m} {k%m}")