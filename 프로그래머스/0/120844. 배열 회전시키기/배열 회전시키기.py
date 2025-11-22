def solution(numbers, direction):
    answer = [0]*len(numbers)
    if direction == "right":
        for i in range(len(numbers)):
            answer[(i + 1) % len(numbers)] = numbers[i]
    if direction == "left":
        for i in range(0,len(numbers)):
            answer[i-1]=numbers[i]

    return answer
