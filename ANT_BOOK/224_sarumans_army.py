N = int(input())
R = int(input())
X = list(map(int, input().split()))

i = 0
ans = 0
while (i < N):
    # カバーされていない左端の点
    s = X[i]
    i += 1

    while (i < N and X[i] - R <= s):
        i+=1
    
    # 新しい点の位置
    p = X[i - 1]

    while (i < N and X[i] <= p + R):
        i+=1

    ans+=1

print(ans)

    
