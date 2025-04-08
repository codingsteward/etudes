N, K = (int(i) for i in input().split())

def paint_balls(N, K):

    def helper(i, prev):
        # number ways to paint ith ball, given prev 
        if i == N:
            return K-1 if prev != None else K
        total = 0
        for k in range(K):
            if k != prev:
                a = helper(i+1, k)
                total += a
        return total
    return helper(1, None)


# print(paint_balls(N, K))

def paint_dp(N, K):

    paint_balls = [[0 for _ in range(K)] for _ in range(N)]
    for k in range(K):
        paint_balls[0][k] = 1
        paint_balls[N-1][k] = 1
    
    for i in range(1, N):
        total_k = sum(paint_balls[i-1])
        for k in range(K):
            paint_balls[i][k] = total_k - paint_balls[i-1][k]

    return sum(paint_balls[-1])

print(paint_dp(N, K))

