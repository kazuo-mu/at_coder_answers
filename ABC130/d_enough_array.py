N, K = map(int, input().split())
A = list(map(int, input().split()))

n_all = N * (N + 1) // 2

# Ans = 全てのケース - K未満になるケース

l = 0
r = 0

under_k = []
_sum = 0

for i in range(N):
    
    l = i
    
    # lは一つずつ進む。一つ前の分を引く
    if l != 0:
        _sum -= A[l-1]

    while (r <= N-1) and (_sum + A[r] < K):
        _sum += A[r]
        r+=1
    
    # rが何個進んだかを記録
    under_k.append(r-l)


n_not = sum(under_k)

ans = n_all - n_not

print(ans)


    