N = int(input())
W = list(map(int, input().split()))

min_diff = 10000

for i in range(1, N):
    left = W[:i]
    right = W[i:]

    diff = abs(sum(left) - sum(right))

    if min_diff > diff:
        min_diff = diff

print(min_diff)
