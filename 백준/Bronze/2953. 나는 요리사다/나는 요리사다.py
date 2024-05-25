score_board = [list(map(int,input().split())) for _ in range(5)]
answer = [0]*5
for i in range(len(score_board)):
    for score in score_board[i]:
        answer[i]+=score
print(f"{answer.index(max(answer))+1} {max(answer)}")
