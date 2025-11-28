def solution(my_string):
    answer = ''
    vowel={'a','i','o','e','u'}
    for alpha in my_string:
        if alpha not in vowel:
            answer+=alpha
    return answer