from sudoku import Sudoku

puzzle = """
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

def test_num_in_row():
    game = Sudoku(puzzle)
    assert game.num_in_row(9, 3)

def test_num_not_in_row():
    game = Sudoku(puzzle)
    assert not game.num_in_row(1, 3)

def test_num_in_col():
    game = Sudoku(puzzle)
    assert game.num_in_col(9, 3)

def test_num_not_in_row():
    game = Sudoku(puzzle)
    assert not game.num_in_col(3, 3)

def test_num_in_subgrid():
    game = Sudoku(puzzle)
    assert game.num_in_subgrid(9, 4, 3)

def test_num_not_in_subgrid():
    game = Sudoku(puzzle)
    assert not game.num_in_subgrid(2, 4, 3)

possibilities = [{2, 3}, {8, 2}, {8, 3, 7}, {2, 3, 5, 7, 9}, set(), {2, 3, 4, 5, 7, 9}, set(), {3, 4, 5, 8, 9}, {9, 3}, set(), set(), set(), set(), {3, 6, 7}, {2, 3, 6, 7}, {1, 7}, {1, 3}, {1, 3}, set(), {8, 1}, {8, 1, 3, 7}, {9, 3, 5, 7}, {9, 3, 4, 7}, {3, 4, 5, 7, 9}, {1, 4, 7, 8, 9}, {1, 3, 4, 5, 8, 9}, set(), set(), set(), set(), {9, 3}, set(), set(), {9, 4}, set(), {9, 3}, set(), set(), {1, 9}, {9, 5, 6, 7}, {9, 6, 7}, {9, 5, 6, 7}, {1, 9}, set(), set(), {1, 2, 9}, set(), {1, 9}, set(), set(), {9, 3}, set(), {1, 3, 9}, set(), set(), {8, 1, 4}, {1, 3, 6, 8, 9}, {1, 2, 3, 6, 9}, {9, 3, 4, 6}, {2, 3, 4, 6, 9}, {8, 1, 2, 9}, {8, 1, 9}, set(), {1, 9}, {1, 5}, {1, 6, 9}, {1, 2, 6, 9}, {9, 6}, set(), set(), set(), set(), {1, 3, 9}, {8, 1, 4}, set(), {1, 3, 6, 7, 9}, set(), {3, 4, 6, 7, 9}, {8, 1, 9}, {8, 1, 9}, {1, 6, 9}]

def test_num_in_row_possibilities():
    game = Sudoku('')
    game._possibilities = possibilities
    assert game.num_in_row_possibilities(9, 3, 6)

def test_num_in_row_possibilities2():
    possibilities = [{2, 3}, {8, 2, 7}, {8, 3, 7}, {2, 3, 5, 7, 9}, set(), {2, 3, 4, 5, 7, 9}, set(), {3, 4, 5, 8, 9}, {9, 3}, set(), set(), set(), set(), {3, 6, 7}, {2, 3, 6, 7}, {1, 7}, {1, 3}, {1, 3}, set(), {8, 1, 7}, {8, 1, 3, 7}, {9, 3, 5, 7}, {9, 3, 4, 7}, {3, 4, 5, 7, 9}, {1, 4, 7, 8, 9}, {1, 3, 4, 5, 8, 9}, set(), set(), {7}, set(), {9, 3, 7}, set(), set(), {9, 4}, set(), {9, 3}, set(), set(), {1, 9, 7}, {9, 5, 6, 7}, {9, 6, 7}, {9, 5, 6, 7}, {1, 9}, set(), set(), {1, 2, 9}, set(), {1, 9}, set(), set(), {9, 3}, set(), {1, 3, 9}, set(), set(), {8, 1, 4}, {1, 3, 6, 8, 9}, {1, 2, 3, 6, 9}, {9, 3, 4, 6}, {2, 3, 4, 6, 9}, {8, 1, 2, 9}, {8, 1, 9}, set(), {1, 9}, {1, 5}, {1, 6, 9}, {1, 2, 6, 9}, {9, 6}, set(), set(), set(), set(), {1, 3, 9}, {8, 1, 4}, set(), {1, 3, 6, 7, 9}, set(), {3, 4, 6, 7, 9}, {8, 1, 9}, {8, 1, 9}, {1, 6, 9}]
    game = Sudoku('')
    game._possibilities = possibilities
    game.print_possibilities()
    assert game.num_in_row_possibilities(7, 3, 3)

def test_num_not_in_row_possibilities():
    game = Sudoku('')
    game._possibilities = possibilities
    assert not game.num_in_row_possibilities(4, 3, 6)

def test_num_in_col_possibilities():
    game = Sudoku('')
    game._possibilities = possibilities
    assert game.num_in_col_possibilities(9, 3, 6)

def test_num_not_in_col_possibilities():
    game = Sudoku('')
    game._possibilities = possibilities
    assert not game.num_in_col_possibilities(9, 7, 1)

def test_num_in_subgrid_possibilities():
    possibilities = [set([1, 2]), set(), set(), set(), set(), set(), set(), set(), set(), set([1, 3]), set(), set([5]), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()]
    game = Sudoku('')
    game._possibilities = possibilities
    assert game.num_in_subgrid_possibilities(1, 0, 0)

def test_exclude_num_in_subgrid_possibilities():
    possibilities = [set() for _ in range(81)]
    game = Sudoku('')
    possibilities[game._get_box_index(3, 3)].add(1)
    possibilities[game._get_box_index(5, 3)].add(1)
    possibilities[game._get_box_index(5, 5)].add(1)
    possibilities[game._get_box_index(4, 6)].add(1)
    possibilities[game._get_box_index(4, 8)].add(1)
    game._possibilities = possibilities
    assert game.num_in_subgrid_possibilities(1, 5, 3)

def test_num_not_in_subgrid_possibilities():
    game = Sudoku('')
    game._possibilities = possibilities
    assert not game.num_in_subgrid_possibilities(2, 5, 0)
