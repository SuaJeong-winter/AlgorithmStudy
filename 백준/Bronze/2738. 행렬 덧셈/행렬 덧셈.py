n,m = map(int,input().split())  #n은 열, m은 행
a = []
for i in range(n):
  a.append(list(map(int,input().split())))

b = []
for i in range(n):
  b.append(list(map(int,input().split())))

for i in range(n):
  for j in range(m):
    print(a[i][j]+b[i][j], end=" ")
  print()