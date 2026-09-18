#Board representation, movement validation.
class Board:
        
    def __init__(self, board=None):
        if board is None:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]
        else:
             self.grid = board #user's board
        self.rows = []
        self.columns = []
        self.box = []
        for i in range(9):
            self.rows.append(set())
            self.columns.append(set())
            self.box.append(set())

        self.build_board()

    def index_in_box(self, r, c):
        return (r//3)*3 + (c//3)
    
    def build_board(self):
        "We get specific board from an user, we need to initialize it first."
        for r in range(9):
            for c in range(9):
                value = self.grid[r][c]
                if value != 0:
                    box_index = self.index_in_box(r,c)
                    self.rows[r].add(value)
                    self.columns[c].add(value)
                    self.box[box_index].add(value)

    def is_valid(self, r,c,value):
        "Now, we need to check,whether this board is properly built."
        box_index = self.index_in_box(r,c)

        if value in self.rows[r] or value in self.columns[c] or value in self.box[box_index]:
            return False
        return True


    def place_number(self,r, c, new_value):
        if self.is_valid(r,c,new_value):
            self.grid[r][c] = new_value
            box_index = self.index_in_box(r,c)

            self.rows[r].add(new_value)
            self.columns[c].add(new_value)
            self.box[box_index].add(new_value)
            return True
        
        return False

    def remove_number(self, r, c):
        "Delete specific number. (Important for back-tracking.)"
        val = self.grid[r][c]

        if val != 0:
            box_index = self.index_in_box(r,c)

            self.rows[r].remove(val)
            self.columns[c].remove(val)
            self.box[box_index].remove(val)

            self.grid[r][c] = 0

    

