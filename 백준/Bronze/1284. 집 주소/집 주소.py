import sys

while(1):
    request=sys.stdin.readline().rstrip()
    if request=='0':
        break
    else:
        sum=2+(len(request)-1)
        for i in range(len(request)):
            if request[i]=='0':
                sum+=4
            elif request[i]=='1':
                sum+=2
            else:
                sum+=3
        print(sum)