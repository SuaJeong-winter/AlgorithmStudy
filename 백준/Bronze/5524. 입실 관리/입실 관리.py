import sys

num=int(sys.stdin.readline())
for _ in range(num):
    word=sys.stdin.readline().rstrip()
    print(word.lower())