def solution(polynomial):
    answer = ''
    x_num=0
    pure_num=0
    numbers=polynomial.split(" + ")
    print(numbers)
    for num in numbers:
        if 'x' in num:
            if num == 'x':
                x_num += 1
            else:
                x_num += int(num[:-1])  # '10x' → '10' -> x이전의 모든 계수를 처리할 수 있도록 num[:-1]
        else:
            pure_num+=int(num)

    # 문자열 조합
    if x_num and pure_num:
        answer= (f"{x_num}x" if x_num > 1 else "x") + " + " + str(pure_num)
    elif x_num:
        answer= f"{x_num}x" if x_num > 1 else "x"
    elif pure_num:
        answer= str(pure_num)
    else:
        answer= "0"
    return answer