from collections import Counter
w = input()

def check_beautiful(w):
    counter = Counter(w)
    return all(counter[key] % 2 == 0 for key in counter)

print("Yes" if check_beautiful(w) else "No")
