# Write your solution here
def print_sudoku(sudoku: list):
    for row_index, row in enumerate(sudoku):
        for col_index, number in enumerate(row):
            if number == 0:
                print("_", end=" ")
            else:
                print(number, end=" ")

            if (col_index + 1) % 3 == 0 and col_index < 8:
                print(" ", end="")

        print()

        if (row_index + 1) % 3 == 0 and row_index < 8:
            print()


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number