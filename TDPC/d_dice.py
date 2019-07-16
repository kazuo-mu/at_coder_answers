
# Dを素因数分解して D = 2**I + 3**J + 5**K を求める
def get_prime_factors(x):
    i = 0
    j = 0
    k = 0

    while x % 2 == 0:
        i += 1
        x /= 2

    while x % 3 == 0:
        j += 1
        x /= 3

    while x % 5 == 0:
        k += 1
        x /= 5

    return (x != 1, i, j, k)


def main():
    N, D = map(int, input().split())
    # dp[MAX_N][MAX_I][MAX_I][MAX_I]ぐらい確保しておく
    dp = [[[[0] * 64 for _ in range(64)] for _ in range(64)] for _ in range(105)]
    f, I, J, K = get_prime_factors(D)

    # 2, 3, 5 以外に素因数がある場合は、サイコロの目の積によって
    # 生み出される数字ではないので、確率を0とする
    if f:
        print(0.0)
        exit()
    
    
    # n回投げた時の, 2, 3, 5の素因数が出現する回数を数える
    dp[0][0][0][0] = 1.0
    for n in range(N):
        for i in range(I+1):
            for j in range(J+1):
                for k in range(K+1):

                    if (dp[n][i][j][k] == 0):
                        continue
                    
                    # I, J, K で抑えることで、Dの倍数が出る確率をdp[N][I][J][K]で表せる
                    dp[n+1][i][j][k]                     += (1/6) * dp[n][i][j][k]   # 1の目がでるとき
                    dp[n+1][min(i+1, I)][j][k]           += (1/6) * dp[n][i][j][k]   # 2の目がでるとき
                    dp[n+1][i][min(j+1, J)][k]           += (1/6) * dp[n][i][j][k]   # 3の目がでるとき
                    dp[n+1][min(i+2, I)][j][k]           += (1/6) * dp[n][i][j][k]   # 4の目がでるとき
                    dp[n+1][i][j][min(k+1, K)]           += (1/6) * dp[n][i][j][k]   # 5の目がでるとき
                    dp[n+1][min(i+1, I)][min(j+1, J)][k] += (1/6) * dp[n][i][j][k]   # 6の目がでるとき

    print(dp[N][I][J][K])


if __name__ == '__main__':
    main()
