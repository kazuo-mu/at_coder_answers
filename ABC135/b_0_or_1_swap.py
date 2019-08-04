N = int(input())
P = list(map(int, input().split()))

E = list(range(1,N+1))

d = [0 if p == e else 1 for p, e in zip(P, E)]

if sum(d) == 0 or sum(d) == 2:
    print('YES')
else:
    print('NO')