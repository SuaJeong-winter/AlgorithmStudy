number = list(map(int,input().split()))
sum = 0
for num in number:
    sum+=num*num
print(sum%10)