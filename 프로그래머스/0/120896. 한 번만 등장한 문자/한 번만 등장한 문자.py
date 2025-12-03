#문자열 s에서 한 번만 등장한 문자들만 모아서
#알파벳 순으로 나열해서 문자열로 출력하기

def solution(s):
    answer = ''
    only_one=[]
    for alpha in s:
        if s.count(alpha)==1:
            only_one.append(alpha)
    s_one= sorted(only_one)
    answer="".join(s_one)
    return answer