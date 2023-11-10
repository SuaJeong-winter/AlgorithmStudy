word=input()
alpha=[0]*26

for i in range(len(word)):
    position=ord(word[i])-97
    alpha[position]+=1

for i in range(len(alpha)):
    print(alpha[i],end=" ")