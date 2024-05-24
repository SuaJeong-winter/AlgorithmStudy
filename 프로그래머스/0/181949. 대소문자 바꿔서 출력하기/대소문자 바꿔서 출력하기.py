str = input()
result=""
for alpha in str:
    if ord(alpha)<91:
        result+="".join(alpha.lower())
    else:
        result+="".join(alpha.upper())
print(result)