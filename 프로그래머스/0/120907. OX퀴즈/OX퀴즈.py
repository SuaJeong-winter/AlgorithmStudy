#수식이 옳다면 O, 틀렸다면 X를 return

def solution(quiz):
    answer = []
    for number in quiz:
        val = number.split()
        if val[1] == "-":
            ans = int(val[0]) - int(val[2])
        elif val[1] == "+":
            ans = int(val[0]) + int(val[2])
        if str(ans) == val[4]:
            answer.append("O")
        else:
            answer.append("X")
    return answer