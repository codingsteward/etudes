N = input()
M = input()

zeroes = len(M)-1
if zeroes >= len(N):
    # if equal it's 0.rest
    # if more
    print("0." + "0" * (zeroes-len(N)) + N)
else:
    i = len(N)-zeroes
    all_zero = True
    decimals = []
    for j in range(len(N)-1, i-1, -1):
        if N[j] != '0':
            all_zero = False
        if not all_zero:
            decimals.append(N[j])
    print(N[:i] if all_zero else N[:i] + '.' + "".join(decimals[::-1]))
