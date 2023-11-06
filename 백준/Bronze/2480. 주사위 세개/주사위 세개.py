import sys

dice_list = [0]*6
a,b,c = map(int,sys.stdin.readline().split())

dice_list[a-1]+=1
dice_list[b-1]+=1
dice_list[c-1]+=1

if 3 in dice_list:
    print(10000+(dice_list.index(3)+1)*1000)
elif 2 in dice_list:
    print(1000+(dice_list.index(2)+1)*100)
elif 1 in dice_list:
    max_dot= list(filter(lambda x:dice_list[x]==1, range(len(dice_list))))
    print((max(max_dot)+1)*100)