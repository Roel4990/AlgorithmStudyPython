T = int(input())
def solve(S):
    for i in range(len(S)):
        if S[i:] == S[i:][::-1]: 
            return S + S[:i][::-1]

for _ in range(T):
    S = input().strip()
    print(solve(S))
