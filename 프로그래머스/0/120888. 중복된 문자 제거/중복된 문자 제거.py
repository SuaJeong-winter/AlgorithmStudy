def solution(my_string):
    answer = ''
    for alpha in my_string:
        if alpha not in answer:
            answer+=alpha

    return answer