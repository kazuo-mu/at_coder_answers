K, X = map(int, input().split())

l = range(max(X-K+1, -1000000), min(X+K,1000000+1))

print(' '.join(map(str, l)))