from collections import defaultdict

class Solution():
    def __init__(self):
        # box size
        self.n = 3
        # row size
        self.N = self.n * self.n
        # lambda function to compute box index
        self.box_index = lambda row, col: (row // self.n) * self.n + col // self.n

        # init rows, columns and boxes
        self.rows = [defaultdict(int) for i in range(self.N)]
        self.columns = [defaultdict(int) for i in range(self.N)]
        self.boxes = [defaultdict(int) for i in range(self.N)]

    def init_board(self, board):
        self.board = board

        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] != '.':
                    d = int(self.board[i][j])
                    self.place_number(d, i, j)

        self.sudoku_solved = False
        self.backtrack()

    def solveSudoku(self, board):
        self.init_board(board)

    def could_place(self, d, row, col):
        """
        Check if one could place a number d in (row, col) cell
        """
        return not (d in self.rows[row] or d in self.columns[col] or \
            d in self.boxes[self.box_index(row, col)])

    def place_number(self, d, row, col):
        """
        Place a number d in (row, col) cell
        """
        self.rows[row][d] += 1
        self.columns[col][d] += 1
        self.boxes[self.box_index(row, col)][d] += 1
        self.board[row][col] = str(d)

    def backtrack(self, row = 0, col = 0):
        """
        Backtracking
        """
        # if the cell is empty
        if self.board[row][col] == '.':
            # iterate over all numbers for 1 to 9
            for d in range(1, 10):
                if self.could_place(d, row, col):
                    self.place_number(d, row, col)
                    self.place_next_number(row, col)
                    # if sudoku is solved, there is no need to backtrack
                    # since the single unique solution is promised
                    if not self.sudoku_solved:
                        self.remove_number(d, row, col)

    def place_next_number(self, row, col):
        """
        Call backtrack function in recursion
        to continue to place numbers
        till the moment we have a solution
        """
        # if we're in the last cell 
        # than means we have the solution
        if col == self.N - 1 and row == self.N - 1:
            self.sudoku_solved = True
        # if not yet
        else:
            # if we're in the end of the row
            # go to the next row
            if col == self.N - 1:
                self.backtrack(row + 1, 0)
            # go to the next column
            else:
                self.backtrack(row, col + 1)

    def remove_number(self, d, row, col):
        # self.rows[row][d] -= 1
        # self.columns[col][d] -= 1
        # self.boxes[self.box_index(row, col)][d] -= 1
        del self.rows[row][d]
        del self.columns[col][d]
        del self.boxes[self.box_index(row, col)][d]
        self.board[row][col] = '.'

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s = Solution()
    s.init_board(board)
    print(s.board)