import copy

n = int(input())
a = list(map(int, input().split()))

max_a = max(a)


def gcd(n, m):
    if m == 0:
        return n
    
    return gcd(m, n % m)


# 事前処理
# あらかじめ、左端からi個でgcdを計算しておく
# 同様に右からも
l = [0] * n
r = [0] * n

l[0] = a[0]
r[-1] = a[-1]

for i in range(0, n-1):
    l[i+1] = gcd(l[i], a[i+1])

for i in range(n-1, 0, -1):
    r[i-1] = gcd(r[i], a[i-1])


tmp = 0
ans = 0

for i in range(n):
    if i == 0:
        tmp = r[i+1]
    elif i == n-1:
        tmp = l[i-1]
    else:
        tmp = gcd(l[i-1], r[i+1])
    
    ans = max(ans, tmp)

print(ans)