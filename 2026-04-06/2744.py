S = input()
result = ""
for i in range(len(S)):
    if S[i].islower():
        result += S[i].upper()
    else:
        result += S[i].lower()
print(result)