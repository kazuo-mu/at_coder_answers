N, M = map(int, input().split())

line = []
for _ in range(M):
    line.append(tuple(map(int, input().split())))

cliques = []

for i in range(pow(2, N)):
    clique = []
    for j in range(N):
        if (i >> j) & 1:
            clique.append(j+1)
    cliques.append(clique)            


max_clique = 0
for clique in cliques:
    n = len(clique)

    is_clique = True

    for i in range(n):
        for j in range(i+1, n):

            if (clique[i], clique[j]) not in line:
                is_clique = False
                break

        if not is_clique:
            break

    if is_clique:
        max_clique = max(max_clique, len(clique))

print(max_clique)