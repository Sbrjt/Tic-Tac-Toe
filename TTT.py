from os import system
from random import choice

grid = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
pos = list(range(1, 10))
cmpmarks, usrmarks = [], []
win = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

mark = input('Enter your mark: ')
print(
    'Remember your choices:\n'
    ' 1 | 2 | 3 \n'
    ' 4 | 5 | 6 \n'
    ' 7 | 8 | 9 '
)


def update():
        print(
        f'{grid[0]} | {grid[1]} | {grid[2]} \n'
        f'{grid[3]} | {grid[4]} | {grid[5]} \n'
        f'{grid[6]} | {grid[7]} | {grid[8]}'
    )

def usr():
    a = int(input('Enter move: '))
    try:
        pos.remove(a)
    except:
        a = int(input('Enter valid move! '))
        pos.remove(a)
    system('cls')
    grid[a - 1] = mark
    usrmarks.append(a)


def cmp():
    if k != 4:
        if mark in ['o','O','0']:
            mark2 = 'x'
        else:
            mark2 = 'o'
        b = choice(pos)
        grid[b - 1] = mark2
        pos.remove(b)
        cmpmarks.append(b)


def check():
    for i in win:
        if i <= set(usrmarks):
            print('You WIN :)')
            return True
        if i <= set(cmpmarks):
            print('Computer WINS :[')
            return True


for k in range(5):
    usr()
    cmp()
    update()
    if check():
        break

print('Game Over.')
