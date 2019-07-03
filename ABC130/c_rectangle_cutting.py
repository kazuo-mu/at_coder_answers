W, H, x, y = map(int, input().split())

if (x * 2 == W and y * 2 == H):
    res = '1'
else:
    res = '0'

area = W * H / 2

print('{} {}'.format(area, res))