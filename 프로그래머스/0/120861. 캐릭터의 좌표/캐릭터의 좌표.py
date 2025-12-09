#[0,0]에서 시작했을 때 keyinput에 따라 이동했을 때 최종 위치를 return
#이때 board의 크기를 벗어난 방향키는 무시함

x_val = [-1, 1, 0, 0]
y_val = [0, 0, 1, -1]
direction = ['left', 'right', 'up', 'down']

def solution(keyinput, board):
    answer = []
    nx, ny = 0, 0
    for idx, direct in enumerate(keyinput):
        for i in range(len(direction)):
            if direct == direction[i]:
                temp_x = nx + x_val[i]
                temp_y = ny + y_val[i]

                
                if -1*(board[0] // 2) <= temp_x <= board[0] // 2 and -1*(board[1] // 2) <= temp_y <= board[1] // 2:
                    nx, ny = temp_x, temp_y
    answer = [nx, ny]
    return answer
