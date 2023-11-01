data = [int(input()) for _ in range(28)]

for index in range(1,31):
    if index not in data:
        print(index)