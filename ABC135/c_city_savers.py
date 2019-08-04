import copy

N = int(input())
A = list(map(int, input().split()))  # N+1
B = list(map(int, input().split()))

d_A = copy.deepcopy(A)

ans = 0

for i in range(N):

    if A[i] <= B[i]:
        B[i] -= A[i]
        A[i] = 0
    else:
        A[i] -= B[i]
        B[i] = 0

    if B[i] > 0 and A[i+1] > 0:
        A[i+1] -= min(B[i], A[i+1])


ans = sum([_a - a for a,_a in zip(A, d_A)])


print(ans)