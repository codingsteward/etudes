a, b, c = (s for s in input().split())

def opposite(direction):
    if direction == "North":
        return "South"
    if direction == "South":
        return "North"
    if direction == "East":
        return "West"
    if direction == "West":
        return "East"

def right(direction):
    if direction == "North":
        return "West"
    if direction == "South":
        return "East"
    if direction == "West":
        return "South"
    if direction == "East":
        return "North"

if b == opposite(a) and c == right(a): # go straight and c is right of a
    print("YES")
elif b == opposite(right(a)) and (c == right(a) or c == opposite(a)):
    print("YES")
else:
    print("NO")
