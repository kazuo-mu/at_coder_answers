N, K = map(int, input().split())

probs = []
for i in range(1, N+1):
    
    a = i
    n = 0
    while a < K:
        a *= 2
        n += 1

    p = (1/N) * (1/2)**n
    probs.append(p)

print(sum(probs))