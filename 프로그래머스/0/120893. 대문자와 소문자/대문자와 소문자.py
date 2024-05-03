def solution(my_string):
    answer = ''
    for i in my_string:
        if ord(my_string[i]<91):
            answer += my_string[i].lower
        else:
            answer+=my_string[i].upper

    return answer