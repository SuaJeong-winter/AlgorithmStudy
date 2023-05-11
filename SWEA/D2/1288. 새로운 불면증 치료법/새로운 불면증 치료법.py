T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num= int(input())  #초기값
    start=1 #num*start로 배수값을 만들 수 
    sheep = [0]*10 #1부터 0 까지 모든 수를 보는지 카운팅하는 1차 배열
    
    while min(sheep)<=0:  #리스트의 모든 값이 1이상일 때 while문 탈출
        snum=str(num*start)  #num을 문자열로 바꿔준다, 배수값은 여기서 만들어짐
        for i in range(len(snum)):
            sheep[int(snum[i])]+=1
        start+=1
    print(f"#{test_case} {snum}")
    
    
    # ///////////////////////////////////////////////////////////////////////////////////

          