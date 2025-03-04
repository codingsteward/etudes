s = input()

def check_string(s):
    for i in range(len(s)):
        if i+1 < len(s):
            if s[i] == s[i+1]:
                return (i+1, i+2)
        if i+2 < len(s):
            if s[i] == s[i+2]:
                return (i+1, i+3)
    return (-1, -1)

a, b = check_string(s)
print(a, b)
