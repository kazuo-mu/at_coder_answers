n = int(input())
a = list(map(int, input().split()))
k = int(input())

def dfs(i, sum):
    if (i == n): return sum == k

    # a[i] を使わない場合
    if dfs(i+1, sum):
        return True 

    # a[i] を使う場合
    if dfs(i+1, sum+a[i]):
        return True
    
    return False


if dfs(0, 0):
    print('Yes')
else:
    print('No')
