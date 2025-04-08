s = input()

# try all possible

def many_formula(s):
    total = 0
    def helper(i, num, prev_sum):
        nonlocal total
        if i == len(s):
            total += prev_sum + num
            return
        
        # either break now or later
        helper(i+1, int(s[i]), prev_sum+num)
        helper(i+1, num*10+int(s[i]), prev_sum)

    helper(1, int(s[0]), 0)
    return total

print(many_formula(s))
