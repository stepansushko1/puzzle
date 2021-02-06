def horizontal_check(board: list):
    """ Check if board are ready for game by its row. Return True of False
    >>> print(horizontal_check(board = ["**** ****","***1 ****","**  3****",\
        "* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***",\
            "  2  ****"]))
    True
    """
    for _, value in enumerate(board):
        lst_of_nums = []
        row = list(value)
        for _, value2 in enumerate(row):
            if value2.isdigit():
                lst_of_nums.append(value2)
        if len(lst_of_nums) != len(set(lst_of_nums)):
            return False
    return True


def vertical_check(board: list):
    """ Check if board are ready for game in columns. Return True of False
    >>> print(vertical_check(board = ["**** ****","***1 ****","**  3****",\
        "* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***",\
            "  2  ****"]))
    False
    """
    for idx in range(len(board)):
        lst_of_nums = []
        for idx2 in range(len(board)):
            if board[idx2][idx].isdigit():
                lst_of_nums.append(board[idx2][idx])
        if len(lst_of_nums) != len(set(lst_of_nums)):
            return False

    return True


def color_check(board: list):
    """ Check if board are ready for game by its colors. Return True of False
    >>> print(color_check(board = ["**** ****","***1 ****","**  3****",\
    "* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***",\
        "  2  ****"]))
    True
    """

    first_column = 4
    last_column = 8
    first_row = 0
    last_row = 4
    idx = 0
    idx2 = 8

    while first_column != 0:
        lst_of_nums = []

        for i in range(first_column, last_column):
            if board[i][idx].isdigit():
                lst_of_nums.append(board[i][idx])

        for i in range(first_row, last_row):
            if board[idx2][i].isdigit():
                lst_of_nums.append(board[idx2][i])

        first_column -= 1
        last_column -= 1

        first_row += 1
        last_row += 1

        idx += 1
        idx2 -= 1

        if len(lst_of_nums) != len(set(lst_of_nums)):
            return False

    return True

def validate_board(board: list):
    """ Check if board are generaly ready for game. Return True of False
    >>> print(validate_board(board = ["**** ****","***1 ****","**  3****",\
        "* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***",\
            "  2  ****"]))
    False
    """
    if horizontal_check(board) and vertical_check(board) and\
            color_check(board):
        return True
    return False
