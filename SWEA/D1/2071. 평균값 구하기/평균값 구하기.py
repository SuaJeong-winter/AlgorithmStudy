T=int(input())
for test_case in range(1,T+1):
    numbers=list(map(int,input().split()))
    sum=0
    for num in numbers:
        sum+=num

    print(f"#{test_case} {round(sum/10)}")