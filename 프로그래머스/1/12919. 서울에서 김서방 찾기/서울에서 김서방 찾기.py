def solution(seoul):
    answer  = ''
    for i in range(len(seoul)):
        if "Kim" in seoul:
            answer = (f'김서방은 {seoul.index("Kim")}에 있다')
            break
    return answer