import sys

place,perpeople=map(int,sys.stdin.readline().split())
a,b,c,d,e = list(map(int,sys.stdin.readline().split()))
total=place*perpeople

for news in [a,b,c,d,e]:
    print(news-total, end=" ")