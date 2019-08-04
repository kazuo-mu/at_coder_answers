D = int(input())
N = int(input())

S = str(N)
mod = 1000000007

dp = [[[0] * D for _ in range(2)] for _ in range(len(S)+1)]
# dp[桁数][N未満確定フラグ][sum % D] := 3で割れる総数

dp[0][0][0] = 1

for i in range(len(S)):
    d_i = int(S[i])
    for j in range(2):
        for k in range(D):
            # 前digitまででN未満かどうか確定していない場合は、当該digitを超えないように
            for l in range(9+1 if j else d_i + 1):
                dp[i+1][j or int(l < d_i)][(k + l) % D] += dp[i][j][k]
                

print((dp[len(S)][1][0] -1 + dp[len(S)][0][0]) % mod)

# N>=1だが、全て0の場合は加算してしまっているので、1を引く
# dp[len(S)][0][0]は、NがDで割れるならば1が入っている
# PythonだとTLEになる...
