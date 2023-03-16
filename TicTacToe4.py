def hello():
    welcome_text = "Добро пожаловать в Крестики - Нолики\n"
    rules = "" \
            "Для того, чтобы сделать ход,\n" \
            "введите  Д В Е  координаты в виде  Ц Е Л Ы Х  чисел через  П Р О Б Е Л,\n" \
            "соответствующие ряду и столбцу на игровом поле.\n" \
            "      --------------\n" \
            "      Например: 1 0\n" \
            "      --------------\n" \
            "Победителем становится первый игрок,\n" \
            "выстроивший 3 символа в ряд (Х или О):\n" \
            "по вертикали, по горизонтали либо по диагонали\n"
    good_luck = "У Д А Ч И :)\n"
    print(welcome_text, rules, good_luck, sep="- - - - - - - - - - - - - - - - - - -\n")


board = [[" ", " ", " "] for i in range(3)]


def show_board():
    print(f"    0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        print(f"{i} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("---------------")


def ask_coord():
    while True:
        line, col = map(int, input("Введите координаты клетки: ").split())
        if line > 2 or line < 0 or col > 2 or col < 0:
            print("Координаты находятся за пределами поля. Введите числа от 0 до 2!")
        else:
            if board[line][col] != " ":
                print("Клетка занята. Выберите другую клетку!")
            else:
                return line, col


def check_victory():
    x = ["X", "X", "X"]
    o = ["O", "O", "O"]

    victory_combs = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]

    for i in range(8):
        if victory_combs[i] == x:
            print("КРЕСТИКИ ПОБЕДИЛИ!")
            return False
        if victory_combs[i] == o:
            print("НОЛИКИ ПОБЕДИЛИ!")
            return False


def game():
    hello()
    show_board()
    turn = 0
    while True:
        turn += 1

        if turn % 2 == 0:
            print("Ходят Нолики!")
            line, col = ask_coord()
            board[line][col] = "O"
        else:
            print("Ходят Крестики!")
            line, col = ask_coord()
            board[line][col] = "X"

        show_board()

        if turn >= 3:
            if check_victory() is False:
                break

        if turn == 9:
            print("У ВАС НИЧЬЯ!")
            break


game()
