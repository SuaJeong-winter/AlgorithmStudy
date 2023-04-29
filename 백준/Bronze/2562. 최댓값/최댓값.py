list=[0]*9
for i in range(len(list)):
    list[i]=int(input())
maxnum=max(list)
print(maxnum)
print(list.index(maxnum)+1)