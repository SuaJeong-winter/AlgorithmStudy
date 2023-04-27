num = int(input())
result = 1
if (num==0):
  print(result)
else:
  for i in range(num):
    result *=(i+1)
  print(result)