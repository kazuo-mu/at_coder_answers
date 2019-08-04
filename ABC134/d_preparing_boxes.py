N = int(input())

A = list(map(int, input().split()))

B = [0] * (N+1)

for i in range(N, 0, -1):
    
    x = 2
    _sum = 0
    for j in range(i+i, N+1, i):    
        _sum ^= B[j]

    B[i] = _sum ^ A[i-1]

ans = []
for i in range(1, len(B)):
    if B[i]:
        ans.append(i)

if ans:
    print(len(ans))
    print(' '.join(map(str, ans)))
else:
    print(0)
