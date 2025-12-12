def solution(my_string):
    answer = 0       # 최종 합을 저장할 변수
    numbers = ""

    for num in my_string:
        if num.isdigit():
            numbers += num       # 숫자면 누적
        elif numbers:
            answer += int(numbers)  # 숫자 끝났을 때 누적합에 더함
            numbers = ""            # 초기화

    if numbers:
        answer += int(numbers)  # 마지막 숫자가 남아있다면 더함

    return answer
