slist = [0]*30
for _ in range(28):
    student=int(input())
    slist[student-1] = 1
for i in range(30):
  if slist[i]==0:
    print(i+1)