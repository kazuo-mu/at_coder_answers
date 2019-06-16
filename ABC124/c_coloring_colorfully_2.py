s = list(map(int, input()))

expected = []

for i in range(len(s)):
    if (i % 2 == 0):
        expected.append(0)
    else:
        expected.append(1)

union = []

for i in range(len(s)):
    union.append((s[i] + expected[i]) % 2)

cnt_0 = union.count(0)
cnt_1 = union.count(1)

print(min(cnt_0, cnt_1))