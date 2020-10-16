from math import sqrt

class Sudoku:

    DIGITS = GRID_ROWS = GRID_COLS = 9
    BOX_LENGTH = int(sqrt(GRID_COLS))

    def __init__(self, puzzle_txt):
        self._grid = self._populate_grid(puzzle_txt)
        self._possibilities = [set() for _ in self._grid]

    def _populate_grid(self, puzzle_txt):
        grid = []
        rows = puzzle_txt.strip().split('\n')
        for r in rows:
            grid.extend(r.strip().split(' '))
        return grid

    def _get_box_index(self, row, column):
        return column + Sudoku.GRID_COLS * row

    def get_box(self, row, column):
        # self._check_bounds(row, column) TODO check that row and column are in appropriate range
        return self._grid[self._get_box_index(row, column)]

    def set_box(self, num, row, column):
        # self._check_bounds(row, column) TODO check that row and column are in appropriate range
        self._grid[self._get_box_index(row, column)] = str(num)

    def get_possible_nums(self, row, column):
        return self._possibilities[self._get_box_index(row, column)]

    def clear_possible_nums(self, row, column):
        self._possibilities[self._get_box_index(row, column)] = set()

    def add_possible_num(self, num, row, column):
        self._possibilities[self._get_box_index(row, column)].add(num)
        
    def remove_possible_num(self, num, row, column):
        if num in self._possibilities[self._get_box_index(row, column)]:
            self._possibilities[self._get_box_index(row, column)].remove(num)

    def num_in_row(self, num, row):
        start_index = Sudoku.GRID_COLS * row 
        end_index = start_index + Sudoku.GRID_COLS
        return str(num) in self._grid[start_index : end_index]

    def num_in_col(self, num, col):
        return str(num) in (self.get_box(i, col) for i in range(Sudoku.GRID_ROWS))

    def _get_subgrid_index_range(self, row, col):
        # self._check_bounds(row, column) TODO check that row and column are in appropriate range
        box_length = Sudoku.BOX_LENGTH
        for b in range(box_length):
            if row >= box_length * b and row < box_length * (b + 1):
                row_start = box_length * b
                row_end = row_start + box_length
                break
        for b in range(box_length):
            if col >= box_length * b and col < box_length * (b + 1):
                col_start = box_length * b
                col_end = col_start + box_length
                break
        return [(row_start, row_end), (col_start, col_end)]


    def num_in_subgrid(self, num, row, col):
        # self._check_bounds(row, column) TODO check that row and column are in appropriate range
        (row_start, row_end), (col_start, col_end) = self._get_subgrid_index_range(row, col)
        subgrid = set()
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                subgrid.add(self.get_box(i, j))
        return str(num) in subgrid

    def num_in_row_possibilities(self, num, row, except_col, exclude_subgrid=False):
        exclusion_check = lambda j: j != except_col
        if exclude_subgrid:
            (row_start, row_end), (col_start, col_end) = self._get_subgrid_index_range(row, except_col)
            exclusion_check = lambda j: not (j >= col_start and j < col_end)
            
        for j in range(Sudoku.GRID_COLS):
            if exclusion_check(j):
                possibilities = self.get_possible_nums(row, j)
                if num in possibilities:
                    return True
        return False

    def num_in_col_possibilities(self, num, except_row, col, exclude_subgrid=False):
        exclusion_check = lambda i: i != except_row
        if exclude_subgrid:
            (row_start, row_end), (col_start, col_end) = self._get_subgrid_index_range(except_row, col)
            exclusion_check = lambda i: not (i >= row_start and i < row_end)
        for i in range(Sudoku.GRID_ROWS):
            if exclusion_check(i):
                possibilities = self.get_possible_nums(i, col)
                if num in possibilities:
                    return True
        return False

    def num_in_subgrid_possibilities(self, num, row, col, exclude_row=False, exclude_col=False):
        # self._check_bounds(row, column) TODO check that row and column are in appropriate range
        assert (exclude_row and exclude_col) == False, 'Only one of exclude_row or exclude_col can be set to True'
        exclusion_check = lambda i, j: (i != row or j != col)
        if exclude_row:
            exclusion_check = lambda i, j: (i != row)
        if exclude_col:
            exclusion_check = lambda i, j: (j != col)
        (row_start, row_end), (col_start, col_end) = self._get_subgrid_index_range(row, col)
        subgrid = set()
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                if exclusion_check(i, j):
                    subgrid.update(self.get_possible_nums(i, j))
        return num in subgrid

    def print_puzzle(self):
        padding = 4 # account for lines in printing
        to_print = ''
        for i in range(Sudoku.GRID_ROWS):
            if i % Sudoku.BOX_LENGTH == 0:
                to_print += '- ' * (Sudoku.GRID_COLS + padding) + '\n'
            for j in range(Sudoku.GRID_COLS):
                if j % Sudoku.BOX_LENGTH == 0:
                    to_print += '| '
                to_print += self.get_box(i, j) + ' '
            to_print = to_print[:-1] + ' |\n'
        to_print += '- ' * (Sudoku.GRID_COLS + padding) + '\n'
        print(to_print)

    def print_possibilities(self):
        padding = 4 # account for lines in printing
        to_print = ''
        for i in range(Sudoku.GRID_ROWS):
            if i % Sudoku.BOX_LENGTH == 0:
                to_print += '- ' * (Sudoku.GRID_COLS + padding) + '\n'
            for j in range(Sudoku.GRID_COLS):
                if j % Sudoku.BOX_LENGTH == 0:
                    to_print += '| '
                pn = self.get_possible_nums(i, j)
                to_print += str('*' if len(pn) == 0 else pn) + ' '
            to_print = to_print[:-1] + ' |\n'
        to_print += '- ' * (Sudoku.GRID_COLS + padding) + '\n'
        print(to_print)

    def generate_possibilities(self):
        for n in range(1, Sudoku.DIGITS + 1):
            for i in range(Sudoku.GRID_ROWS):
                for j in range(Sudoku.GRID_COLS):
                    if self.get_box(i, j) == '*' and \
                       not self.num_in_row(n, i) and \
                       not self.num_in_col(n, j) and \
                       not self.num_in_subgrid(n, i, j):
                           self.add_possible_num(n, i, j)

    def remove_possibilities(self, num, row, col):
        self.clear_possible_nums(row, col)
        # update row
        for j in range(Sudoku.GRID_COLS):
            if j != col:
                self.remove_possible_num(num, row, j)
        # update col
        for i in range(Sudoku.GRID_ROWS):
            if i != row:
                self.remove_possible_num(num, i, col)
        # update subgrid
        (row_start, row_end), (col_start, col_end) = self._get_subgrid_index_range(row, col)
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                if i != row or j != col:
                    self.remove_possible_num(num, i, j)

    def remove_row_possibilties_skipping_subgrid(self, num, row, col):
        (row_start, row_end), (col_start, col_end) = self._get_subgrid_index_range(row, col)
        for j in range(Sudoku.GRID_COLS):
            if not (j >= col_start and j < col_end):
                self.remove_possible_num(num, row, j)

    def remove_col_possibilties_skipping_subgrid(self, num, row, col):
        (row_start, row_end), (col_start, col_end) = self._get_subgrid_index_range(row, col)
        for i in range(Sudoku.GRID_ROWS):
            if not (i >= row_start and i < row_end):
                self.remove_possible_num(num, i, col)

    def solve(self):
        is_complete = False
        it = 100
        self.generate_possibilities()
        while not is_complete:
            it -= 1
            is_complete = all(len(p) == 0 for p in self._possibilities) or it <= 0

            for i in range(Sudoku.GRID_ROWS):
                for j in range(Sudoku.GRID_COLS):
                    possibilities = self.get_possible_nums(i, j)
                    for possibility in possibilities:
                        # if this possible number is not anywhere else we've solved that box
                        if (not self.num_in_row_possibilities(possibility, i, j)) \
                                or (not self.num_in_col_possibilities(possibility, i, j)) \
                                or (not self.num_in_subgrid_possibilities(possibility, i, j)):
                            self.set_box(possibility, i, j)
                            self.remove_possibilities(possibility, i, j)
                        if (not self.num_in_subgrid_possibilities(possibility, i, j, exclude_row=True) \
                                and self.num_in_row_possibilities(possibility, i, j, exclude_subgrid=True)):
                                self.remove_row_possibilties_skipping_subgrid(possibility, i, j)
                        if (not self.num_in_subgrid_possibilities(possibility, i, j, exclude_col=True) \
                                and self.num_in_col_possibilities(possibility, i, j, exclude_subgrid=True)):
                                self.remove_col_possibilties_skipping_subgrid(possibility, i, j)

                    if len(possibilities) == 1:
                        num = possibilities.pop()
                        self.set_box(num, i, j)
                        self.remove_possibilities(num, i, j)


if __name__ == '__main__':
    easy_puzzle = """
    * * * * 9 * * 4 *
    * * * 8 * 5 * * 9
    * 8 * 6 * 7 1 * *
    6 5 * 9 3 * 4 * *
    7 2 * 4 5 1 * 8 6
    * * 4 * 6 8 * 9 5
    * * 2 1 * 4 * 7 *
    8 * * 5 * 6 * * *
    * 6 * * 2 * * * *
    """
    game = Sudoku(easy_puzzle)
    print('Puzzle to be solved:')
    game.print_puzzle()
    game.solve()
    print('Solved puzzle:')
    game.print_puzzle()

    medium_puzzle = """
    * * * * 1 * 6 * *
    5 9 4 8 * * * * *
    6 * * * * * * * 2
    8 * 5 * 2 1 * 6 *
    4 3 * * * * * 2 8
    * 6 * 4 8 * 5 * 7
    7 * * * * * * * 5
    * * * * * 8 3 7 4
    * * 2 * 5 * * * *
    """
    game = Sudoku(medium_puzzle)
    print('Medium puzzle to be solved:')
    game.print_puzzle()
    game.solve()
    print('Solved puzzle:')
    game.print_puzzle()

    hard_puzzle = """
    * 1 * 6 * * * 5 *
    4 * * * 3 * * 6 *
    8 * * * 1 * 7 3 *
    1 * 2 * * * * * *
    * 7 * 3 * 8 * 4 *
    * * * * * * 6 * 5
    * 2 1 * 6 * * * 4
    * 8 * * 7 * * * 6
    * 5 * * * 3 * 2 *
    """
    game = Sudoku(hard_puzzle)
    print('Hard puzzle to be solved:')
    game.print_puzzle()
    game.solve()
    print('Solved puzzle:')
    game.print_puzzle()

    
    evil_puzzle = """
    * * 7 * * 8 1 * 4
    * * * * * * 3 * 6
    3 * * * 5 * * * *
    * * 9 8 1 * * * *
    * 5 * * 3 * * 6 *
    * * * * 2 9 4 * *
    * * * * 4 * * * 2
    7 * 4 * 7 * * * 6
    9 * 8 1 * * 7 * *
    """

    game = Sudoku(evil_puzzle)
    print('Evil puzzle to be solved:')
    game.print_puzzle()
    game.solve()
    print('Solved puzzle:')
    game.print_puzzle()
