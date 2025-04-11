import sys

while True:
    try:
        N, *seq = (int(i) for i in input().split())
        seen = [False]*(N-1)
        for i in range(len(seq)-1):
            diff = abs(seq[i]-seq[i+1])
            if diff < N:
                seen[diff-1] = True
        if all(seen):
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break


