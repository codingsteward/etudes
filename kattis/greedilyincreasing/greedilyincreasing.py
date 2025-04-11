N = int(input())
permutation = [int(i) for i in input().split()]

gis = [permutation[0]]

for i in range(1, len(permutation)):
    if permutation[i] > gis[-1]:
        gis.append(permutation[i])
print(len(gis))
print(" ".join(map(str, gis)))
