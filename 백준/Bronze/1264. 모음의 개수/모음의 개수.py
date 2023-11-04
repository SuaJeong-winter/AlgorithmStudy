while(1):
    data = input()
    if data=="#":
        break
    else:
        cnt=0
        for i in range(len(data)):
            if data[i] in ['a','e','i','o','u','A','E','I','O','U']:
                cnt+=1
            else:
                pass
        print(cnt)