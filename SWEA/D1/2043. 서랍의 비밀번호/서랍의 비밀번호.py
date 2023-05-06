#비밀번호 P, 초기값 K 입력받기 
p, k = map(int, input().split())
cnt=1
while k != p:
    cnt+=1
    k+=1
    if p == k:
        break
print(cnt)

    