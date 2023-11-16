T = int(input())
for test_case in range(1,T+1):
    num=int(input())
    numbers= list(map(int,input().split()))
    s_numbers=sorted(numbers)
    print(f"#{test_case}", end=" ")
    for n in range(num):
        print(s_numbers[n],end=" ")
    print()