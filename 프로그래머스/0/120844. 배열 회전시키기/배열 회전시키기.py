def solution(numbers, direction):
    answer = []
    if direction == "right":
        for i in range(len(numbers)):
            answer[(i + 1) % len(numbers)] = numbers[i]
    if direction == "left":
        for i in range(0,len(numbers)+1):
            if i != 0:
                answer[i] = numbers[i+1]
            else:
                answer[len(numbers)-1] = numbers[0]

    return answer
