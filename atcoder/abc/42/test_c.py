N, K = (int(i) for i in input().split())
nums = [int(i) for i in input().split()]
available_digits = [i for i in range(10) if i not in nums]

def find_smallest_N():

    def check(guess):
        while guess != 0:
            last_digit = guess % 10
            if last_digit in nums:
                return False
            guess //= 10
        return True

    # try every digit until 10 * N
    for guess in range(N, 10*N+1):
        if check(guess):
            return guess

# def find_smallest_N():
#     if N[0] == '9':
#         first_digit = available_digits[0]
#         if first_digit == 0 and len(available_digits) > 1:
#             first_digit = available_digits[1]
#         return(first_digit * 10**(len(N)))
#     res = 0
#     is_greater = False
#     for i in range(len(N)):
#         # find smallest digit
#         if is_greater:
#             res += available_digits[0] * 10**(len(N)-i-1)
#         else:
#             for digit in available_digits:
#                 if digit >= int(N[i]):
#                     smallest_digit = digit
#                     is_greater = digit > int(N[i])
#                     break
#             res += smallest_digit * 10**(len(N)-i-1)
#     return res
# 
print(find_smallest_N())
