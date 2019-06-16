r, D, x2000 = map(int, input().split())
 
def rec(n):
    if n == 0:
        return x2000
    else:
        return r * rec(n-1) - D


for i in range(1, 11):
    print(rec(i))
