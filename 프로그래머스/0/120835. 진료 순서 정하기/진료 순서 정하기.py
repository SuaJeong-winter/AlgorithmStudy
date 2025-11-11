def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency,reverse=True)
    for score in emergency:
        for s_score in sorted_emergency:
            if score == s_score:
                answer.append(sorted_emergency.index(score) + 1)

    return answer
