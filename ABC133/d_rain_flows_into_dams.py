N = int(input())
A = list(map(int, input().split()))

B = []

# b1 = - A1 + A2 - A3 ... - AN (奇数個) が式変形で求められる
b1 = 0
for i in range(len(A)):
    if i % 2 == 0:
        b1 += A[i]
    else:
        b1 -= A[i]

B.append(b1)

# B[i] = 2 * A[i-1] - B[i-1] (式変形により)
for i in range(1, N):
    bi = 2 * A[i-1] - B[i-1] 
    B.append(bi)

print(' '.join(map(str, B)))
