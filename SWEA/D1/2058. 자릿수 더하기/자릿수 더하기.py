num=int(input())
sum=0
while(1):
  sum+=num%10
  num=num//10  
  if num%10 ==0:
    break
print(sum)