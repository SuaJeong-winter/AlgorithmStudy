def solution(number):
    value=0
    for num in number:
        value+=int(num)
    return value%9