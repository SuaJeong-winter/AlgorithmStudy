burgers=[]
sodas=[]
for i in range(3):
    burger=int(input())
    burgers.append(burger)
for j in range(2):
    soda=int(input())
    sodas.append(soda)

print(min(burgers)+min(sodas)-50)