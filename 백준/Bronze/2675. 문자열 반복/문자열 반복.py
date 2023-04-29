T=int(input())
for _ in range(T):
    re,s=input().split()
    for i in range(len(s)):
            print(s[i]*int(re), end="")
    print()