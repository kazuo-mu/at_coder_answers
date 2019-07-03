#最大公約数
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

 #最小公倍数
def lcm(a,b):
    return a*b//gcd(a,b)

A, B, C, D = map(int, input().split())

# 0 => A-1 で割りきれる
cnt_c = (A-1) // C
cnt_d = (A-1) // D

cnt_cd = (A-1) // lcm(C, D)

cnt_a = cnt_c + cnt_d - cnt_cd

# 0 => Bで割りきれる
cnt_c2 = B // C
cnt_d2 = B // D
cnt_cd2 = B // lcm(C, D)

cnt_b = cnt_c2 + cnt_d2 - cnt_cd2

cnt_ab = cnt_b - cnt_a

cnt_n = B - A + 1

print(cnt_n - cnt_ab)