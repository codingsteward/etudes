N, M = (int(i) for i in input().split())
dance = []
for i in range(N):
    dance.append(list(input()))


print(dance)
count = 0
for j in range(M):
    if all(dance[i][j] == '_' for i in range(N)):
        print(i, j)
        count += 1
print(count)

