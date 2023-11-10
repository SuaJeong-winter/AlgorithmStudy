import sys

Astudent= list(map(int,input().split()))
Bstudent = list(map(int,input().split()))

if sum(Astudent)>sum(Bstudent):
    print(sum(Astudent))
else:
    print(sum(Bstudent))