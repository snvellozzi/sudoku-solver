board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bd):

    # Base case of recursion
    find = find_empty(bd)
    if not find:
        return True     # Solution Found
    else:
        row, col = find

    # Checks if number is valid solution in board
    for i in range(1, 10):
        if valid(bd, i, (row, col)):
            bd[row][col] = i    # Adds valid number into board

            if solve(bd):
                return True

            bd[row][col] = 0

    return False


def valid(bd, number, pos):

    # Checks rows
    for i in range(len(bd[0])):
        if bd[pos[0]][i] == number and pos[1] != i:
            return False

    # Checks columns
    for i in range(len(bd)):
        if bd[i][pos[1]] == number and pos[0] != i:
            return False

    # Checks which box currently in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Loops through boxes
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bd[i][j] == number and (i, j) != pos:     # Checks if elements in box are equal to number added
                return False
    return True


def print_board(bd):

    for i in range(len(bd)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bd[i][j])
            else:
                print(str(bd[i][j]) + " ", end="")


def find_empty(bd):

    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return i, j     # row, col order

    return None     # No blank squares


print("//////////Before/////////////")
print_board(board)
solve(board)
print("//////////After/////////////")
print_board(board)
