def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1*denom2+numer2*denom1
    denom = denom1*denom2
    for i in range(denom,0,-1):
        if numer%i==0 and denom%i==0:
            numer=numer//i
            denom=denom//i
        else:
            pass
    answer.append(numer)
    answer.append(denom)
    return answer
