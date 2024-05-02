import sys

def solution(numbers):
    for i in range(1,numbers+1):
        titles = sys.stdin.readline().rstrip()
        print(f'{i}. {titles}')

numbers = int(sys.stdin.readline())
solution(numbers)


    