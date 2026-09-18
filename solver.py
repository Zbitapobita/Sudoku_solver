#Logic behind program. Aka 'Backtracking'
from board import Board

class SudoSolver:

    def __init__(self, board: Board):
        self.board = board

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r,c)
        return None 
    def solve(self):
        empty_position = self.find_empty()
        if not empty_position:
            return "Congratulations! Sudoku is solved!"

        row, column = empty_position

        for num in range(1,10):
            if self.is_valid(row, column, num):
                if self.solve():
                    True
            self.board.remove_number(row, column)
        return False