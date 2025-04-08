a = input()
b = input()
c = input()

a_ptr = b_ptr = c_ptr = 0
curr_ptr = 'a'
while True:
    if curr_ptr == 'a':
        if a_ptr == len(a):
            break
        curr_ptr = a[a_ptr]
        a_ptr += 1
    elif curr_ptr == 'b':
        if b_ptr == len(b):
            break
        curr_ptr = b[b_ptr]
        b_ptr += 1
    elif curr_ptr == 'c':
        if c_ptr == len(c):
            break
        curr_ptr = c[c_ptr]
        c_ptr += 1

print(curr_ptr.upper())
