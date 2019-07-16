L, R = map(int, input().split())

mod = 2019
R = min(R, L + mod + 1)

ans = 100000000+5
for i in range(L, R):
    for j in range(i+1, R+1):
        ans = min(ans, i * j % mod)

print(ans)
