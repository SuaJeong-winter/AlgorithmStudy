#문자열을 출력하되 num1부터 num2에 해당하는 문자열은 서로 바꿔서 출력
def solution(my_string, num1, num2):
    answer = my_string[:num1]+my_string[num2]+my_string[num1+1:num2]+my_string[num1]+my_string[num2+1:]
    return answer