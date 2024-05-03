def solution(x):
    answer = True
    sum = 0
    x = str(x)
    for i in range(len(x)):
        sum += int(x[i])

    if int(x)%sum ==0:
        answer = True
    else:
        answer = False
    return answer