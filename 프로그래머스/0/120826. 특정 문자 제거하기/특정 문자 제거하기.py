def solution(my_string, letter):
    answer = ""
    for index in my_string:
        if letter == index:
            pass
        else:
            answer+= "".join(index)

    return answer