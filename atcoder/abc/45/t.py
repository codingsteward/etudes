N = int(input())
points = [None]*N
for i in range(N):
  points[i] = [int(j) for j in input().split()]

prev = [points[0][0], points[0][1], points[0][2]]
for i in range(1, N):
  new_prev = [0]*3
  for j in range(3):
    for k in range(3):
      if j != k:
        new_prev[j] = max(new_prev[j], prev[k]+points[i][j])
  prev = new_prev
print(max(prev))
