PLAYER_MOVES = "*"
RABBIT_HOLE = "R"
TEA_BAGS_TO_COLLECT = 10


def get_field(row_count):
    matrix = []
    for row in range(row_count):
        row = input().split()
        matrix.append(row)
    return matrix


def get_alice_position(matrix):
    matrix_size = len(matrix)
    for r in range(matrix_size):
        for c in range(matrix_size):
            if matrix[r][c] == "A":
                return r, c


def get_directions(move):
    directions = {
        "left": (0, -1),
        "up": (-1, 0),
        "right": (0, 1),
        "down": (1, 0),
    }

    return directions[move]


def in_range(row, col, matrix):
    matrix_size = len(matrix)
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def is_rabbit_hole_position(row, col, matrix):
    return matrix[row][col] == RABBIT_HOLE


def alice_mark_move(row, col, matrix):
    matrix[row][col] = PLAYER_MOVES


def print_field(field):
    for row in field:
        print(' '.join(row))


rows = int(input())

field = get_field(rows)

alice_position_row, alice_position_col = get_alice_position(field)

tea_bags_collected= 0
move = input()
while move:
    row, col = get_directions(move)
    alice_mark_move(alice_position_row, alice_position_col, field)
    if not in_range(alice_position_row + row, alice_position_col + col, field):
        print("Alice didn't make it to the tea party.")
        break
    alice_position_row += row
    alice_position_col += col
    if is_rabbit_hole_position(alice_position_row, alice_position_col, field):
        alice_mark_move(alice_position_row, alice_position_col, field)
        print("Alice didn't make it to the tea party.")
        break
    if field[alice_position_row][alice_position_col].isdigit():
        tea_bags_collected += int(field[alice_position_row][alice_position_col])
    if tea_bags_collected >= TEA_BAGS_TO_COLLECT:
        print("She did it! She went to the party.")
        alice_mark_move(alice_position_row, alice_position_col, field)
        break
    move = input()

print_field(field)

