h,m,s = map(int,input().split())
sec = int(input())

h+=sec//3600
m+=(sec%3600)//60
s+=(sec%3600)%60

if s>=60:
    m+=1
    s%=60

if m>=60:
    h+=1
    m%=60

if h>=24:
    h%=24


print(h,m,s)