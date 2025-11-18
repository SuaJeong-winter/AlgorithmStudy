def solution(hp):

    garmy= hp//5
    sarmy=(hp%5)//3
    warmy=(hp-(5*garmy+3*sarmy))//1
    answer = garmy+sarmy+warmy

    return answer