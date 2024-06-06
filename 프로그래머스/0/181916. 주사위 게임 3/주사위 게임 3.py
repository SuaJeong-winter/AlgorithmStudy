def solution(a, b, c, d):
    dice=[a,b,c,d]
    abcd=dict()

    for num in dice:
        # 주사위들의 숫자 넣기
        if num not in abcd:
            abcd[num]=1
        else:
            abcd[num]+=1

    #조건에 따라 case 나누기
    abcd=sorted(abcd,key=lambda x: abcd[x])

    if len(abcd)==1:
        return 1111*a
    elif len(abcd)==2:
        if dice.count(abcd[0]) in [1,3]:
            return (10*abcd[1]+abcd[0])**2
        else:
            return(abcd[0]+abcd[1])*abs(abcd[0]-abcd[1])
    elif len(abcd)==3:
        return abcd[0]*abcd[1]
    else:
        return min(dice)