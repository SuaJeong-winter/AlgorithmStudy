
def solution(numbers):
    answer = 0
    val = 0
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            tmp = numbers[i] * numbers[j]
            print(numbers[i], numbers[j], tmp)
            if val < tmp:
                val = tmp
    answer=val

    return answer


