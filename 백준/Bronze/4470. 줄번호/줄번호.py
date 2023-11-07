import sys

num= int(sys.stdin.readline())
for i in range(1,num+1):
    sentence=sys.stdin.readline().rstrip()
    print(f"{i}. {sentence}")