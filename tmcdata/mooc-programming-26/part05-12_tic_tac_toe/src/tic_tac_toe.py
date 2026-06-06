# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    # Check if coordinates are within bounds
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False

    # Check if the square is empty
    if game_board[y][x] != "":
        return False

    # Place the piece
    game_board[y][x] = piece
    return True