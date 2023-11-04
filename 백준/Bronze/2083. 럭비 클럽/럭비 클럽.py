import sys

while(1):
    name, age, weight = sys.stdin.readline().split()
    if name=="#" and age=="0" and weight=="0":
        break
    else:
        if int(age)>17 or int(weight)>=80:
            print(f"{name} Senior")
        else:
            print(f"{name} Junior")