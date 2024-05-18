def solution(emergency):
    answer = [0] * len(emergency)
    grade = 1
    fixed_line = reversed(sorted(emergency))
    f_line = list(fixed_line)
    for i in range(len(f_line)):
        answer[emergency.index(f_line[i])] = grade
        grade += 1
    return answer