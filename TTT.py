from os import system
from random import choice

l = [' '] * 9  # game board
pos = list(range(1, 10))  # available positions on game board
pc_marks, usr_marks = set(), set()
winning_combinations = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

usr_mark = input('Choose your mark (o or x): ')

if usr_mark == 'x':
    pc_mark = 'o'
elif usr_mark == 'o':
    pc_mark = 'x'
else:
    print("Invalid!")
    exit

print(
    'Remember your choices:\n'
    ' 1 | 2 | 3 \n'
    ' 4 | 5 | 6 \n'
    ' 7 | 8 | 9 '
)


def print_game_board():
    system('cls')

    print(
        f'{l[0]} | {l[1]} | {l[2]} \n'
        f'{l[3]} | {l[4]} | {l[5]} \n'
        f'{l[6]} | {l[7]} | {l[8]}'
    )


def usr_turn():
    x = int(input('Enter move: '))
    if x in pos:
        pos.remove(x)
    else:
        print('Invalid move!')
    l[x - 1] = usr_mark
    usr_marks.add(x)


def pc_turn():
    x = choice(pos)  # random choice
    l[x - 1] = pc_mark
    pos.remove(x)
    pc_marks.add(x)


def usr_wins():
    for i in winning_combinations:
        if i.issubset(usr_marks):
            print('You WIN :)')
            return True

    return False


def pc_wins():
    for i in winning_combinations:
        if i.issubset(pc_marks):
            print('Computer WINS :[')
            return True

    return False


# Main game loop
for i in range(1, 6):
    usr_turn()
    print_game_board()
    if usr_wins():
        break

    if i == 5:
        break  # only 9 places on game board

    pc_turn()
    print_game_board()
    if pc_wins():
        break

print('Game Over.')
