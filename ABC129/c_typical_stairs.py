n, m = map(int, input().split())

broken = [0 for _ in range(n+1)]
for i in range(m):
    a = int(input())
    broken[a] = True

    
mod = 1000000007
dp = [0 for _ in range(n+2)]

dp[n] = 1
for i in range(n-1, -1, -1):
    if(broken[i]):
        dp[i] = 0
        continue

    dp[i] = (dp[i+1] + dp[i+2]) % mod

print(dp[0])