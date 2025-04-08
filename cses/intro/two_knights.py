N = int(input())

def slow_knight(N):
    for i in range(1, N+1):
        # try all possible ways
        # number ways to put two knights = k^2 * (k^2-1)

        # first knight got i * i choices
        # second knight got i*i - 1 choices
        total_ways = (i**4 - i**2)//2

        # number ways where knight touches another knight
        attack = 0
        for r in range(i):
            for c in range(i):
                # consider knight position at board[r][c]

                # top, down
                if r-2 >= 0:
                    attack += int(c-1 >= 0)
                    attack += int(c+1 < i)

                if r+2 < i:
                    attack += int(c-1 >= 0)
                    attack += int(c+1 < i)

                if c-2 >= 0:
                    attack += int(r-1 >= 0)
                    attack += int(r+1 < i)

                if c+2 < i:
                    attack += int(r-1 >= 0)
                    attack += int(r+1 < i)
        # print(int(total_ways-attack/2))

def fast_knight(N):
    # for each i, compute incrementally the additional row and column
    # essentially a DP ?
    prev_count = 0
    for i in range(1, N+1):
        if i == 1:
            prev_count = 0
        elif i == 2:
            prev_count = 6
        else:
            # consider extra column, row and square
            attack = 0
            for r in range(1, i+1): # check new column, check left side
                if i-2 >= 1:
                    attack += int(r-1 >= 1)
                    attack += int(r+1 <= i)

            for c in range(1, i): # check new row except last avoid double count
                if i-2 >= 1:
                    attack += int(c-1 >= 1)
                    attack += int(c+1 <= i)
            # missing twenty two
            # first knight has 5 places to go, second knight has 4 + 4
            first_knight = (2*i-1)
            additional = first_knight * (i-1) * (i-1)
            new_squares_only = first_knight * (first_knight-1) // 2
            prev_count = prev_count + additional+new_squares_only- attack
        print(prev_count)

def faster_knight(N):
    # total ways 
    for i in range(1, N+1):
        squares = i*i
        total = squares * (squares-1) // 2
        blocks = (i-1)*(i-2)
        print(total-4*blocks)

faster_knight(N)
