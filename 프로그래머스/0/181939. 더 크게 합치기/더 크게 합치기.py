def solution(a, b):
    result1 = str(a)+str(b)
    result2 = str(b)+str(a)
    if result1>= result2:
        return int(result1)
    else:
        return int(result2)
