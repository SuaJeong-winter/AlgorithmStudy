num=int(input())
numbers=list(map(int,input().split()))
sort_num=sorted(numbers)
print(sort_num[num//2])