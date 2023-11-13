T=int(input())

for _ in range(1,T+1):
    score_board=[0]*101 #0부터 100까지의 점수판
    test=int(input())
    score_list=list(map(int,input().split()))
    for s in range(len(score_list)):
        score_board[score_list[s]]+=1  #0~100점이 각각 몇 개씩 있는지 확인

    max_score=[i for i, v in enumerate(score_board) if v==max(score_board)]
    print(f"#{test} {max(max_score)}")



