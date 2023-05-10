#나중에 꼭 다시 풀어볼 것

pic = [[0 for i in range(5)] for j in range(5)]
for i in range(5):
  for j in range(5):
    if i==j:
      pic[i][j]="#"
    else:
      pic[i][j]="+"

for i in pic:
  for j in i:
    print(j,end="")
  print()

