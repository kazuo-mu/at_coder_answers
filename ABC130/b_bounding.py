N, X = map(int, input().split())
L = list(map(int, input().split()))

d = [0] * (N+1)

for i in range(1, N+1):
    d[i] = d[i-1] + L[i-1]

ans = sum([1 if dv <= X else 0 for dv in d])

print(ans)
