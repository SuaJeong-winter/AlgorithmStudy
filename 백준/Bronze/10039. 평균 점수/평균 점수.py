import sys

score=[]

for i in range(5):
    students=int(sys.stdin.readline())
    if students<40:
        students=40
    score.append(students)

print(sum(score)//5)