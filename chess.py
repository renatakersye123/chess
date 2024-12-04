"""Defining libraries of possible pieces names"""
white_pieces = ["pawn", "rook"]
black_pieces = ["pawn", "rook", "king", "queen", "bishop", "knight"]

def main(): 
    """DEFINING main function that accounts borad state and also count of placement that white and black pieces have"""
    board_state = get_new_board_state()
    black_count = 0
    white_count = 0

    print_board(board_state)


    while white_count < 1:
        white_position = get_user_input("White can choose pawn or rook.", white_pieces)
        if white_position is None:
            print("Invalid input. Please choose pawn or rook and place them in correct format. I.E. pawn a1")
            continue
        else:
            print()
        white_count += 1
        place_piece(board_state,white_position,{"pawn":"O", "rook": "R"}[white_position[0]])


    while black_count <= 16:
        black_position = get_user_input("Black move.", black_pieces)
        if black_count >= 1 and black_position is None:
            print("Ending placement.")
            break 
        elif black_count < 1 and black_position is None:
            print("No black pieces entered.")
            break  

        elif board_state[black_position[1]][black_position[2]] != " ":
            print("Invalid move, there's already a move made there!")
        else:
            place_piece(board_state, black_position, "X")
            black_count += 1

    check_possible_captures(board_state)


###INPUT

def get_user_input(player, pieces):
    """DEFINING input"""
    while True:
        try:
            user_input = input(f"{player}Enter where to place a piece in the format as in example: pawn a1: ").strip().lower()

            if user_input == "done": 
                return None

            piece, coords = user_input.split()
            if piece not in pieces:
                raise ValueError("Input must be in the format: piece a1.")

            x, y = board_coords(coords)
            if 0 <= x <= 7 and 0 <= y <= 7:
                return [piece, x, y]
            else:
                print("Coordinates must be between a-h for columns and 1-8 for rows.")
        except (ValueError, IndexError):
            print("Invalid format. Please enter in the format: pece a1.")

def place_piece(board_state, position, symbol):
    """Places a piece on the board."""
    x, y = position[1], position[2]
    board_state[y][x] = symbol
    print_board(board_state)
    print("Move accepted")


##MOVES AND CAPTURE CALCULATIONS

def check_possible_captures(board_state):
    """Checks and prints possible captures for white pieces."""
    for y in range(8):
        for x in range(8):
            piece = board_state[y][x]
            if piece == "O":
                check_captures(board_state, x, y, possible_takes_pawn, "White pawn")
            elif piece == "R":
                check_captures(board_state, x, y, possible_takes_rook, "White rook")


def check_captures(board_state, x, y, move_state, piece_name):
    """Checks and prints capture opportunities for a specific piece."""
    moves = move_state(board_state, x, y)
    if moves:
        captures = " ".join(f"{get_column_name(capture_x)}{8 - capture_y}" for capture_x, capture_y in moves)
        print(f" Possible capture at {captures}")
    else:
        print("No captures available")


def possible_takes_pawn(board_state, x, y):
    """Defining pawn moves"""
    captures = []
    if 0 <= x-1 < 8 and 0 <= y-1 < 8:
        if board_state[y-1][x-1] == "X":
            captures.append((x-1, y-1))

    if 0 <= x+1 < 8 and 0 <= y-1 < 8:
        if board_state[y-1][x+1] == "X":
            captures.append((x+1, y-1))

    return captures


def possible_takes_rook(board_state, x, y):
    """Returns possible captures for a white rook."""
    captures = []

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        while 0 <= new_x < 8 and 0 <= new_y < 8:
            if board_state[new_y][new_x] == "X":
                captures.append((new_x, new_y))
                break 

            elif board_state[new_y][new_x] != " ":
                break

            new_x, new_y = new_x + dx, new_y + dy

    return captures


#BOARD

def board_coords(coords):
    """Converts 'a5' style coordinates to (x, y) indices."""
    x = ord(coords[0]) - ord('a')
    y = 8 - int(coords[1])
    return x, y


def get_column_name(x):
    """converting column index (0-7) to chess notation (a-h)"""
    return chr(x + ord('a'))

def get_new_board_state():
    """Creates an empty 8x8 chess board."""
    return [[" " for _ in range(8)] for _ in range(8)]


def print_board(board_state):
    """Prints the current state of the board."""
    print("     " + "   ".join(chr(i + ord('a')) for i in range(8)))
    print("   +" + "---+" * 8)
    for i, row in enumerate(reversed(board_state[::-1])):
        print(f" {8 - i} | " + " | ".join(row) + " |")
        print("   +" + "---+" * 8)


"""Calling main function to start program"""
if __name__ == "__main__":
    main()
