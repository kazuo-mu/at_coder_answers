a = int(input())
oturi = 1000 - a

coins = [500, 100, 50, 10, 5, 1]

ans = 0

for coin in coins:
    ans += oturi // coin
    oturi %= coin

print(ans)
