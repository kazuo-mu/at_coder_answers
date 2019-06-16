N, K = map(int, input().split())
V = list(map(int, input().split()))

R = min(N, K)
# 50 = min(100, 50)

ans = 0
# 左から取得する回数をA回, 右からをB回
# として、A + B <= R となるように全探索を行う

def filter_minus(x):
    if x < 0:
        return True
    else:
        return False


# 0, 1 ... 49, 50
for i in range(R+1):
    B = R - i
    # 50 - (0, 1 ... 49, 50) = 50, 49 ... 1, 0
    for j in range(B+1):
        left = V[:i]
        right = V[N-j:]

        k  = R - i - j

        
        values = left + right
        values.sort(reverse=True)

        print(values)

        for _ in range(k):
            if values and values[-1] < 0:
                values.pop() 

        print(values)
        print('------------------')
            
        total_v = sum(values)

        if total_v > ans:
            ans = total_v

print(ans)
