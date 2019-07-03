S = input()
N = len(S)
ans = 0

# 二進数で考えると、0, 1, 10, 11, 100 ... 1111
for i in range(2**(N-1)):
    exp = S[0]

    # 右に一つずつシフトしていき、
    for j in range(1, N):

        # 最初の桁が1であれば（&1でTrue）+, そうでなければスルー
        if (i >> (j-1)) & 1: exp += '+'
        exp += S[j]
        
    ans += eval(exp)

print(ans)
