t = int(input())
for i in range(t):
    row, col = (int(i) for i in input().split())
    if row < col: # start with col
        if col % 2 == 0: # is even, means square number
            col_start = (col-1)*(col-1)+1
            print(col_start+row-1)
        else:
            col_start = col*col
            print(col_start-row+1)
    else:
        if row % 2 == 1:
            row_start = (row-1)*(row-1) + 1
            print(row_start+col-1)
        else:
            row_start = row*row
            print(row_start-col+1)
