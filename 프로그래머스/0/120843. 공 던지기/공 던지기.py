def solution(numbers, k):
    answer = 0
    location=(2*(k-1))%len(numbers)
    answer=numbers[location]
    return answer