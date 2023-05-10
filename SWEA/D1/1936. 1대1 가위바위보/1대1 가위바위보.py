Anum, Bnum = map(int, input().split())
if (Anum==2 and Bnum==1) or (Anum==3 and Bnum==2) or (Anum==1 and Bnum==3) :
    print("A")
elif (Anum==3 and Bnum==1) or (Anum==1 and Bnum==2) or (Anum==2 and Bnum==3):
    print("B")
else:
    pass

