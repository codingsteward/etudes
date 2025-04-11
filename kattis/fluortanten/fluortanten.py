n = int(input())
reluctants = [int(i) for i in input().split()]

# try all insertion.. realise it's prefix/postfix sums?
reluctants.remove(0)

# if insert 0, then 
unhappy = 0
for i in range(len(reluctants)):
    unhappy += (i+2) * reluctants[i]

# 1 swap with 2 => unhappy will change
max_happy = unhappy
for i in range(len(reluctants)):
    unhappy -= reluctants[i]
    max_happy = max(max_happy, unhappy)

print(max_happy)

