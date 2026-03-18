N = int(input())

dp = [0] * (N+1)
dp[1], dp[2] = 1, 1

def fibo(n):
    if dp[n]:
        return dp[n]

    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]

print(fibo(N))
