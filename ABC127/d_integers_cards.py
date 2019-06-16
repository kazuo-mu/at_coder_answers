from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))

BC = []
for _ in range(M):
    BC.append(tuple(map(int, input().split())))

A.sort()

BC.sort(key=lambda x:x[1], reverse=True)

D = deque([])
for bc in BC:
    b = bc[0]
    c = bc[1]

    for _ in range(b):
        D.append(c)

    if len(D) >= N: 
        break

for i in range(N):
    if A[i] < D[0]:
        A[i] = D[0]
        D.popleft()
        if not D:
            break

print(sum(A))