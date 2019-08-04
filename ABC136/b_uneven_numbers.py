N = int(input())

ans = 0
for i in range(1, N+1):
    s = str(i)
    l = len(s)

    if l % 2 != 0:
        ans += 1

print(ans)