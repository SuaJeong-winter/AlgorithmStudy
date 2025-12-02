#문자열 cipher에서 code*n번째의 글자를 합쳐서 해독 문자열을 출력

def solution(cipher, code):
    answer = ''
    for idx in range(code,len(cipher)+1,code):
        answer+=cipher[idx-1]
    return answer