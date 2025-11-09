def solution(money):
    drink= money//5500
    change = money-5500*drink
    answer = [drink,change]
    return answer