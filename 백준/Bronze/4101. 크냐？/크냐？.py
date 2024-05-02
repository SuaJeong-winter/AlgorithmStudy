import sys


def solution(a,b):
    if num1>num2:
        print("Yes")
    else:
        print("No")
    
while(1):
    num1, num2 = map(int,sys.stdin.readline().split())
    if num1 ==0 and num2 ==0:
        break
    else:
        solution(num1,num2)