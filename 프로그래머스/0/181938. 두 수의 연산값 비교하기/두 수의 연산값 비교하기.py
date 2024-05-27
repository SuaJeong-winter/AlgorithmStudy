def solution(a, b):
    result1 = str(a)+str(b)
    if int(result1) >= 2*a*b:
        return int(result1)
    else:
        return 2*a*b