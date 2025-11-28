#대문자는 소문자로, 소문자는 대문자로

def solution(my_string):
    answer = ''
    for alpha in my_string:
        if ord(alpha)<97:
            answer+=''.join(alpha.lower())
        else:
            answer+=''.join(alpha.upper())
    return answer

