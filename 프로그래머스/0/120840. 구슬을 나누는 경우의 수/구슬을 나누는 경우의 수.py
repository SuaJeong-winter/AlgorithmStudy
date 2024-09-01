import math

def solution(balls, share):
    total, dup=1,1
    for upper in range(balls,balls-share,-1):
        total*=upper
    for lower in range(1,share+1):
        dup*=lower
    result1 = total//math.gcd(total,dup)
    result2 = dup//math.gcd(total,dup)
    return result1//result2