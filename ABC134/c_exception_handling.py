import copy

N = int(input())

A = []
for _ in range(N):
    A.append(int(input()))


max1 = max(A)

max_i = A.index(max1)
max2 = max(A[:max_i] + A[max_i+1:])


for i in range(N):
    if A[i] == max1:
        print(max2)

    else:
        print(max1)
