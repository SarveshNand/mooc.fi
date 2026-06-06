# Write your solution here
def row_correct(sudoku: list, row_no: int):
    seen = []

    for number in sudoku[row_no]:
        if number != 0:
            if number in seen:
                return False
            seen.append(number)

    return True


def column_correct(sudoku: list, column_no: int):
    seen = []

    for row in sudoku:
        number = row[column_no]

        if number != 0:
            if number in seen:
                return False
            seen.append(number)

    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    seen = []

    for row in range(row_no, row_no + 3):
        for col in range(column_no, column_no + 3):
            number = sudoku[row][col]

            if number != 0:
                if number in seen:
                    return False
                seen.append(number)

    return True


def sudoku_grid_correct(sudoku: list):
    # Check all rows
    for row in range(9):
        if not row_correct(sudoku, row):
            return False

    # Check all columns
    for col in range(9):
        if not column_correct(sudoku, col):
            return False

    # Check the 9 standard 3x3 blocks
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not block_correct(sudoku, row, col):
                return False

    return True