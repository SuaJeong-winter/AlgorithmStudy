import math

def solution(n):
    gcd_pizza= math.gcd(n,6)
    total_pizza = (n*6)//gcd_pizza
    answer = total_pizza//6

    return answer