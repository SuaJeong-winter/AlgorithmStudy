T=int(input())
for _ in range(T):
    ans=list(input())
    result=0
    score=0
    for i in range(len(ans)):
        if ans[i] == "O":
            score+=1
            result+=score
        elif ans[i]=="X":
            score=0
            result+=0
        else: 
            pass
    print(result)