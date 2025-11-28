def solution(my_string):
    answer = []
    numbers="0123456789"
    for num in my_string:
        if num in numbers:
            answer.append(int(num))
    answer.sort()
    return answer