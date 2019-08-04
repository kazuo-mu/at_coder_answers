
def solve(S):
    
    L = len(S)

    # dp[桁数][N未満フラグ][4 or 9 を含むか]
    dp = [[[0] * 2 for _ in range(2)] for _ in range(32)]

    dp[0][0][0] = 1

    for i in range(L):
        D = int(S[i])

        for j in range(2):
            for k in range(2):
                for d in range(9+1 if j else D+1):
                    dp[i+1][j or int(d < D)][k or int(d in (4, 9))] += dp[i][j][k]

    return dp[L][0][1] + dp[L][1][1]


def main():
    A, B = map(int, input().split())
    print(solve(str(B)) - solve(str(A-1)))

    # N = int(input())
    # print(solve(str(N)))

if __name__ == '__main__':
    main()