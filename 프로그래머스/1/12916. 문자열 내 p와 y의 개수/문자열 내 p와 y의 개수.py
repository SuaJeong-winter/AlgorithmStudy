def solution(s):
    data = s.lower()
    cntp = data.count('p')
    cnty = data.count('y')
    if cntp == cnty:
        return True
    elif cntp==cnty==0:
        return True
    else: 
        return False