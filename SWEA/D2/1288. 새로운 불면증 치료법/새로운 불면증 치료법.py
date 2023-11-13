T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    num_list=[0]*10 #0~9까지의 수를 카운트할 리스트

    k=1
    while(1):
        num1= n*k
        for num in str(num1):
            num_list[int(num)]+=1
        k += 1
        if min(num_list)!=0:
            print(f"#{test_case} {num1}")
            break
