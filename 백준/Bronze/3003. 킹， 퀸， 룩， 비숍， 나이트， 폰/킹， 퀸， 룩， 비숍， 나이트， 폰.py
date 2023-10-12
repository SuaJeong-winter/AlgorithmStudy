pieces = [1,1,2,2,2,8]
my_pieces = input().split()
for i in range(len(pieces)):
    print(pieces[i]-int(my_pieces[i]),end=" ")