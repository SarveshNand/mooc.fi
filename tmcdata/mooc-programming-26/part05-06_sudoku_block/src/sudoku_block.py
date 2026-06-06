# Write your solution here
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