n = int(input())

buttons = []

for i in range(n):
    buttons.append(int(input()))

index = 1
cnt = 0

for i in range(n):
    index = buttons[index-1]
    cnt += 1

    if index == 2:
        print(cnt)
        exit()

print(-1)