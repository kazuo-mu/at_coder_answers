N = int(input())
D = list(map(int, input().split()))

D.sort()

end = N // 2
start = (N // 2) - 1

print(len(range(D[start]+1, D[end]+1)))

