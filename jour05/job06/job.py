class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [['O' for x in range(n)] for y in range(n)]

    def is_safe(self, row, col):
        for i in range(self.n):
            if self.board[row][i] == 'X' or self.board[i][col] == 'X':
                return False
            if row-i >= 0 and col-i >= 0 and self.board[row-i][col-i] == 'X':
                return False
            if row-i >= 0 and col+i < self.n and self.board[row-i][col+i] == 'X':
                return False
            if row+i < self.n and col-i >= 0 and self.board[row+i][col-i] == 'X':
                return False
            if row+i < self.n and col+i < self.n and self.board[row+i][col+i] == 'X':
                return False
        return True

    def solve(self, col):
        if col == self.n:
            return True

        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 'X'

                if self.solve(col+1):
                    return True

                self.board[row][col] = 'O'

        return False

    def print_board(self):
        for row in range(self.n):
            print(' '.join(self.board[row]))

n = int(input("Entrer la valeur de n: "))
queens = NQueens(n)
queens.solve(0)
queens.print_board()