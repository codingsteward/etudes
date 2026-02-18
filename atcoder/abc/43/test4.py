matrix = []

for i in range(5):
    matrix.append(list(input()))

def check(matrix):
    knight = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] != 'k': continue
            knight += 1
            if i-1 >= 0 and j-2 >=0:
                if matrix[i-1][j-2] == 'k': return False
            
            if i-1 >= 0 and j+2 < 5:
                if matrix[i-1][j+2] == 'k': return False
                
            if i-2 >= 0:
                if j-1 >= 0 and matrix[i-2][j-1] == 'k': return False
                if j+1 < 5 and matrix[i-2][j+1] == 'k': return False
            
            if i+1 < 5:
                if j-2 >= 0 and matrix[i+1][j-2] == 'k': return False
                if j+2 < 5 and matrix[i+1][j+2] == 'k': return False
            
            if i+2 < 5:
                if j-1 >= 0 and matrix[i+2][j-1] == 'k': return False
                if j+1 < 5 and matrix[i+2][j+1] == 'k': return False
    return knight == 9

print("valid" if check(matrix) else "invalid")
            
