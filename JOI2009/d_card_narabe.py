from itertools import permutations

n = int(input())
k = int(input())

cards = []
for _ in range(n):
    cards.append(input())

nums = set()
for p in permutations(cards, k):
    num = int(''.join(p))
    nums.add(num)

print(len(nums))