N, M = (int(i) for i in input().split())
sweaters = []
for i in range(N):
    sweaters.append(list(int(j) for j in input().split()))
    
# 1,2,3
ans = []
for i in range(N):
    for j in range(M):
        if i == 0 and j > 0:
            sweaters[i][j] += sweaters[i][j-1]
        elif i > 0:
            if j == 0:
                sweaters[i][j] += sweaters[i-1][j]
            else:
                sweaters[i][j] += sweaters[i][j-1]
                if sweaters[i][j-1] < sweaters[i-1][j]:
                    sweaters[i][j] += (sweaters[i-1][j] - sweaters[i][j-1])
    ans.append(str(sweaters[i][-1]))
print(" ".join(ans))
