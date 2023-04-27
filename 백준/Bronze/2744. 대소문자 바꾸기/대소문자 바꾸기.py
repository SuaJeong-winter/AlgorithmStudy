txt=list(input())
for i in range(len(txt)):
    if 65<=ord(txt[i])<=90:
        print(chr(ord(txt[i])+32), end='')
    if 97<=ord(txt[i])<=120:
        print(chr(ord(txt[i])-32), end='')