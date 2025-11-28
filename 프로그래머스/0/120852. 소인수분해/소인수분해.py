import math

def solution(n):
    answer = []
    std = set()
    for i in range(2, n + 1):
        std.add(math.gcd(i, n))

    for numbers in std:
        cnt = 0
        for num in range(1, numbers + 1):
            if numbers % num == 0:
                cnt += 1
        if cnt == 2:
            answer.append(numbers)
    answer.sort()
    return answer
