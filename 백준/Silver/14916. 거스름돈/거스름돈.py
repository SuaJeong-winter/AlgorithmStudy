import sys

changes = int(sys.stdin.readline())
found = False #정답을 찾았는지에 대한 flag

for i in range(0, changes//2+1): #2원 동전을 사용한 갯수 i: 0개 ~n//2
    if (changes-2*i)%5==0:
        print(i+(changes-2*i)//5)
        found=True
        break
if not found: #found가 False인 경우. 즉, 2원을 changes//2까지 쎃는데도 안될 경우
    print(-1)