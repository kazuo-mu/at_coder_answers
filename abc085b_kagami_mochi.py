N = int(input())

mochi_list = []

for _ in range(N):
    mochi = int(input())
    mochi_list.append(mochi)

mochi_list = set(mochi_list)
mochi_list = list(mochi_list)

print(len(mochi_list))