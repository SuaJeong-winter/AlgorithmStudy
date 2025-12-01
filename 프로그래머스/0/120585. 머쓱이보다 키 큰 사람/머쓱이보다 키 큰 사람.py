def solution(array, height):
    answer = 0
    for person in array:
        if person>height:
            answer+=1
    return answer