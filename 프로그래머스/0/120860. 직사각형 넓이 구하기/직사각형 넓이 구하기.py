#직사각형 네 꼭짓점의 좌표가 주어질 때 직사각형의 넓이를 return

def solution(dots):
    x_vals = [x for x, y in dots]
    y_vals = [y for x, y in dots]
    answer=(max(x_vals) - min(x_vals)) * (max(y_vals) - min(y_vals))
    return answer