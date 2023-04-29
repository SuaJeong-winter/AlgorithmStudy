leftlist = [0]*42
for i in range(10):
    num=int(input())
    leftlist[num%42]+=1
count=0
for j in range(len(leftlist)):
  if leftlist[j] !=0:
    count+=1
  else:
    pass

print(count)
    