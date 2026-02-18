N, t = (int(i) for i in input().split())
A = [int(i) for i in input().split()]

def sum7777(A):
    seen = {}
    for num in A:
        if 7777-num in seen:
            return "Yes"
        seen[num] = True
    return "No"

def checkUnique(A):
    is_unique = len(A) == len(set(A))
    return ("Unique" if is_unique else "Contains duplicate")

def findMajority(A):
    majority = None
    count = 0
    for num in A:
        if num == majority:
            count += 1
        else:
            if count == 0:
                majority = num
                count = 1
            else:
                count -= 1
    
    if A.count(majority) > len(A) // 2:
        return majority
    else:
        return -1

def median(A):
    A.sort()
    middle = (len(A)-1) // 2
    if len(A) % 2 == 0:
        print(A[middle], A[middle+1])
    else:
        print(A[middle])

def sortOrder(A):
    A.sort()
    output = [str(num) for num in A if 100 <= num <= 999]
    if output:
        print(" ".join(output))


if t == 1:
    print(sum7777(A))
elif t == 2:
    print(checkUnique(A))
elif t == 3:
    print(findMajority(A))
elif t == 4:
    median(A)
else:
    sortOrder(A)

