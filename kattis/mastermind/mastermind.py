N, code, guess = input().split()
N = int(N)

chars = [0] * 26
r = s = 0
for i in range(N):
    if code[i] == guess[i]:
        r += 1
    else:
        code_index = ord(code[i]) - ord('A')
        guess_index = ord(guess[i]) - ord('A')
        # if guess is valid, then code -= 1
        if chars[guess_index] > 0:
            s += 1

        if chars[code_index] < 0:
            s += 1
        # AAABBB BBBAAA

        chars[code_index] += 1
        chars[guess_index] -= 1
print(r, s)


