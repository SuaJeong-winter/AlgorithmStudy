def solution(my_string, letter):
    answer = ''
    for alpha in my_string:
        if alpha !=letter:
            answer+=alpha
    return answer