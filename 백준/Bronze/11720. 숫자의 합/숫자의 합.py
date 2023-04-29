N=int(input())
numbers=list(map(int,input()))
sum=0
for i in range(N):
    sum+= numbers[i]
    
print(sum)