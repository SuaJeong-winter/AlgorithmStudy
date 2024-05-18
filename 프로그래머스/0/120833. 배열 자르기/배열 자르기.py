def solution(numbers, num1, num2):
    answer = []
    for index in range(num1, num2+1):
        answer.append(numbers[index])
    return answer