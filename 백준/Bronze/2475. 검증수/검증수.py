def verification(number):
    sum=0
    result=0
    for i in range(len(number)):
      sum+=number[i]*number[i]
    result=sum%10
    return result
    
numberlist=list(map(int,input().split()))
print(verification(numberlist))

        
        
        