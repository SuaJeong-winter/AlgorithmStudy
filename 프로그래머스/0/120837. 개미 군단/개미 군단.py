def solution(hp):
    answer = 0
    while hp!=0:
        if hp>=5:
            answer+=hp//5
            hp=hp-5*answer
        elif hp>=3:
            answer+=hp//3
            hp=hp-3*answer
        elif hp>=1:
            answer+=hp
            hp=0
    return answer