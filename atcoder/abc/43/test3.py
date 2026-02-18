try:
    H, W, N, M = (int(i) for i in input().split())
    matrix = []
    for i in range(H):
        matrix.append(list(int(j) for j in input().split()))

    kernel = []
    for i in range(N):
        kernel.append(list(int(j) for j in input().split()))

    new_matrix = [[0] * (W-M+1) for _ in range(H-N+1)]

# flipping the rows
    for i in range(N//2):
        for j in range(M):
            kernel[i][j], kernel[N-i-1][j] = kernel[N-i-1][j], kernel[i][j]


# flipping the cols
    for j in range(M//2):
        for i in range(N):
            kernel[i][j], kernel[i][M-j-1] = kernel[i][M-j-1], kernel[i][j]

# row by col
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            total = 0
            for x in range(N):
                for y in range(M):
                    # x,y
                    print(x, y, i, j)
                    print(N, M)
                    total += kernel[x][y]*matrix[x+i][y+j]
            new_matrix[i][j] = str(total)

    for row in new_matrix:
        print(" ".join(row))
except Exception as e:
    print(e)
    print(e.args)
    print(matrix)
    raise e
