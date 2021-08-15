t = []
is_X = True
X_win = None
game_finished = False
for i in range(0, 9):
    t.append("_")


def input_c():
    global t
    global is_X
    global game_finished
    global X_win
    if "_" not in t:
        game_finished = True
        return
    while True:
        x, y = input('Enter the coordinates:').split()
        if not x.isdigit() or not y.isdigit():
            print('You should enter numbers!')
            continue
        x, y = [int(x), int(y)]
        if x <= 0 or x > 3 or y <= 0 or y > 3:
            print('Coordinates should be from 1 to 3!')
            continue
        elif t[(x - 1) * 3 + y - 1] != '_':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            if is_X:
                t[(x - 1) * 3 + y - 1] = "X"
            elif not is_X:
                t[(x - 1) * 3 + y - 1] = "O"
            for a in range(0, 7, 3):
                if t[a] == "X" or t[a] == "O":
                    if t[a] == t[a + 1] == t[a + 2]:
                        game_finished = True
                        X_win = is_X
                        return
            for b in range(0, 3):
                if t[b] == "X" or t[b] == "O":
                    if t[b] == t[b+3] == t[b+6]:
                        game_finished = True
                        X_win = is_X
                        return
            if t[4] == "X" or t[4] == "O":
                if t[0] == t[8] == t[4] or t[2] == t[4] == t[6]:
                    game_finished = True
                    X_win = is_X
                    return
            is_X = not is_X
        return




print(f"""---------
| {t[0]} {t[1]} {t[2]} |
| {t[3]} {t[4]} {t[5]} |
| {t[6]} {t[7]} {t[8]} |
---------""")
while not game_finished:
    input_c()
    print(f"""---------
| {t[0]} {t[1]} {t[2]} |
| {t[3]} {t[4]} {t[5]} |
| {t[6]} {t[7]} {t[8]} |
---------""")
else:
    if X_win is None:
        print("Draw")
    elif X_win:
        print("X wins")
    else:
        print("O wins")
