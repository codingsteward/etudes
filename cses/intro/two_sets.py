n = int(input())

total_sum = (n+1)*(n)//2

if total_sum % 2 == 1:
    print("NO")
else:
    # previous group can be paired up
    # left 1
    # but previously group will have odd pair

    # so we give it to another number

    set_one, set_two = [], []
    even_digits = n % 2 == 0
    right = n if even_digits else n-1
    left = 1
    is_set_one = True
    while left < right:
        if is_set_one:
            set_one.append(left)
            set_one.append(right)
        else:
            set_two.append(left)
            set_two.append(right)
        left += 1
        right -= 1
        is_set_one = not is_set_one

    if not even_digits:
        if is_set_one:
            set_one.append(n)
        else:
            set_two.append(n)

    print("YES")
    print(len(set_one))
    print(" ".join(map(str,set_one)))
    print(len(set_two))
    print(" ".join(map(str, set_two)))


