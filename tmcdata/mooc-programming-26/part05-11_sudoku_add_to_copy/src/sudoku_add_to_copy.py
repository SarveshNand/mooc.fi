# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    # Create a copy of the grid
    grid_copy = []

    for row in sudoku:
        grid_copy.append(row.copy())

    # Add the new number to the copy
    grid_copy[row_no][column_no] = number

    return grid_copy