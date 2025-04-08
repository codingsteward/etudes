N = int(input())
K = int(input())
X = int(input())
Y = int(input())

def total_fee():
    return min(N, K) * X + max(N-K, 0) * Y

print(total_fee())
