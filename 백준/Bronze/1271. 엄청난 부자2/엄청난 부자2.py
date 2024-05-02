def solution(coins, creatures):
    money = int(coins)//int(creatures)
    leftover = int(coins)%int(creatures)
    print(money)
    print(leftover)

coins, creatures = input().split()
solution(coins, creatures)