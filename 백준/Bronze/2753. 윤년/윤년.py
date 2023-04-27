xyear = int(input())

if ((xyear%4==0 and xyear%100!=0)or(xyear%400==0)):
    print("1")
else:
  print("0")
        