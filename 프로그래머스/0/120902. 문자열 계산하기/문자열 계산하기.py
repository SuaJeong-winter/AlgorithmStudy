#문자열로 된 수식이 주어질 때, 수식을 계산한 값을 return
#연산자는 +, - 만 존재
#시작과 끝에는 공백이 없다
#0으로 시작하는 숫자는 주어지지 X

def solution(my_string):
    tokens = my_string.split()  # 공백을 기준으로 my_string을 나눔
    print(tokens)  # ['1', '+', '2', '+', '5', '-', '3'] 이렇게 숫자와 연산자가 번갈아 나타남
    answer = int(tokens[0])  # 리스트의 첫번째 항목은 항상 숫자
    for i in range(1, len(tokens), 2):  # 연산자 위치만 반복해서 +, +, -
        op = tokens[i]
        print(op)  # + -> + -> -
        num = int(tokens[i + 1])  # 연산자 뒤에 오는 숫자
        if op == '+':
            answer += num
        elif op == '-':
            answer -= num
    return answer

