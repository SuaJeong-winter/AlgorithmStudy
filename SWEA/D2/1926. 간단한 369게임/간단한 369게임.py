num=input()
cnt=0

for i in range(1, int(num)+1):
    if ('3'in str(i)) or ('6'in str(i)) or ('9'in str(i)):
        ii=str(i)
        for j in range(len(ii)):
            if ('3'in ii[j]) or ('6' in ii[j]) or ('9'in ii[j]):
                cnt+=1
            else:
                continue
        print("-"*cnt, end=" ")
        cnt=0
    else:
        print(i, end= " ")
