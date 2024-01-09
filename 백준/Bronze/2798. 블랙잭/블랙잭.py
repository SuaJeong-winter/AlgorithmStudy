cards, hap = map(int,input().split())
cardsNum = list(map(int,input().split()))

maxNum = 0 
result=0

for num1 in range(cards):
    for num2 in range(num1+1,cards): #시작 인덱스 번호
        for num3 in range(num2+1,cards):  #시작 인덱스 번호
            maxNum=cardsNum[num1]+cardsNum[num2]+cardsNum[num3]
            if maxNum <= hap:
                result = max(result,maxNum)
print(result)