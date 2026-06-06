# Write your solution here
def column_correct(sudoku: list, column_no: int):
    seen = []

    for row in sudoku:
        number = row[column_no]

        if number != 0:
            if number in seen:
                return False
            seen.append(number)

    return True