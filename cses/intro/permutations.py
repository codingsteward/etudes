n = int(input())

def perm(n):
    if n == 1:
        return "1"
    elif n == 2 or n == 3:
        return "NO SOLUTION"

    odd = [str(i) for i in range(1, n+1, 2)]
    even = [str(i) for i in range(2, n+1, 2)]
    return " ".join(even+odd)

print(perm(n))
