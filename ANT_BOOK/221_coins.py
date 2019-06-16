# input
# A
# C1 C5 C10 C50 C100 C500

# sample input
# 620
# 3 2 1 3 0 2

A = int(input())
C = list(map(int, input().split()))

P = [1, 5, 10, 50, 100, 500]


ans = 0

for i in range(len(C)-1, -1, -1):
    # それぞれのコインの最大枚数までしか使わない
    n = min(A // P[i], C[i])
    A -= P[i] * n
    ans += n


print(ans)
