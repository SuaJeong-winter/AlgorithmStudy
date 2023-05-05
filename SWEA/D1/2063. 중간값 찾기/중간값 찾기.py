N =int(input())
numlist = list(map(int, input().split()))
numlist.sort()
print(numlist[N//2])