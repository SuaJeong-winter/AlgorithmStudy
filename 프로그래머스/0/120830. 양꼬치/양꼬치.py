def solution(n, k):
    total = 12000*n + 2000*(k-(n//10) if n >=10  else k)
    return total