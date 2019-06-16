a, b, c = map(int, input().split())

for i in range(a, a*b+1, a):
    if i % b == c:
        print('YES')
        exit()

print('NO')
