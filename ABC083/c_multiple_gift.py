X, Y = map(int, input().split())

k = X

ans = 1
while k * 2 <= Y:
    k = k * 2
    ans += 1

print(ans)