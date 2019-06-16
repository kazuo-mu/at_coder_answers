n = int(input())
s = input()
 
w = [0]
e = [0]
 
tmp_w = 0
tmp_e = 0
 
for i in range(1, n):
 
    j = (n - 1) - i
 
    if (s[i-1] == 'W'):
        w.append(tmp_w + 1)
        tmp_w += 1
    else:
        w.append(tmp_w)
 
    if (s[j+1] == 'E'):
        e.append(tmp_e + 1)
        tmp_e += 1
    else:
        e.append(tmp_e)
 
e.reverse()
 
ans = 10 ** 6 
for i in range(n):
    ans = w[i] + e[i] if w[i] + e[i] < ans else ans
 
print(ans)