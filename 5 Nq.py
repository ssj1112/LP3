n = int(input("Enter the value of N: "))

board = [[0]*n for i in range(n)]

def safe(r, c):
    for i in range(r):
        for j in range(n):
            if board[i][j] == 'Q':
                if j == c or abs(i-r) == abs(j-c):
                    return False
    return True

def solve(r):
    if r == n:
        return True

    for c in range(n):
        if safe(r, c):
            board[r][c] = 'Q'

            if solve(r+1):
                return True

            board[r][c] = 0

    return False

# Place first Queen
board[0][1] = 'Q'

if solve(1):
    print("N-Queens Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists")