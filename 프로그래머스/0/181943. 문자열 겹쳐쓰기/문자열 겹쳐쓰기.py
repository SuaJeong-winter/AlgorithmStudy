def solution(my_string, overwrite_string, s):
    answer = ''
    for i in range(len(my_string)):
        if s<=i<=s+len(overwrite_string)-1:
            answer+="".join(overwrite_string[i-s])
        else:
            answer+="".join(my_string[i])

    return answer