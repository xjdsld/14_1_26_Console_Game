import random
import time

class Pole:
    def __init__(self):
        self.mss = []
        for i in range(10):
            row = []
            for j in range(10):
                row.append('[_]')
            self.mss.append(row)

    def show_pole(self):
        for row in self.mss:
            for cell in row:
                print(cell, ' ', end='')
            print()
        print()

def intro_cat():
    with open("cat.txt", 'r') as file:
        cat_image = file.read()
        print(cat_image)

class ItemSum:
    def __init__(self):
        self.mss_c = []
        self.mss_a = []
        self.mss_d = []
        self.mss_h = []

    def print_user_case(self):
        print('Number of C:', sum(self.mss_c))
        print('Number of A:', sum(self.mss_a))
        print('Number of D:', sum(self.mss_d))
        print('Number of H:', sum(self.mss_h))

    def counter(self, mss, player_pos):
        i, j = player_pos
        cell = mss[i][j]

        if cell == '[C]':
            self.mss_c.append(1)
        elif cell == '[A]':
            self.mss_a.append(1)
        elif cell == '[D]':
            self.mss_d.append(1)
        elif cell == '[H]':
            self.mss_h.append(1)

        if cell in ['[C]', '[A]', '[D]', '[H]']:
            mss[i][j] = '[_]'
            self.print_user_case()

class Player:
    def __init__(self, user_n=0, user_m=0, skin="[U]"):
        self.user_n = user_n
        self.user_m = user_m
        self.skin = skin

    def place(self, field):
        field[self.user_n][self.user_m] = self.skin


class UseCrit:
    def krit(self):
        chance = random.randint(1, 2)
        if chance == 1:
            print('Krit!')
            return True
        else:
            print('No krit')
            return False

    def chance_krittt(self):
        bonus = random.randint(5, 30) / 100
        print('Crit bonus: +' + str(int(bonus * 100)) + '%')
        return bonus


class Cell:
    player = '[U]'
    C = '[C]'
    A = '[A]'
    D = '[D]'
    H = '[H]'
    enemy = '[E]'
    port = '[P]'

class UserHod:
    def user(self, board, item_counter):
        start_user = [0, 0]
        c = Cell()
        board.mss[start_user[0]][start_user[1]] = c.player

        board.show_pole()

        while True:
            move = input('Enter w,s,a,d or q for exit: ')

            if move == 'q':
                print('Exit game')
                break

            new_i = start_user[0]
            new_j = start_user[1]

            if move == 'w' and start_user[0] > 0:
                new_i -= 1
            elif move == 's' and start_user[0] < 9:
                new_i += 1
            elif move == 'a' and start_user[1] > 0:
                new_j -= 1
            elif move == 'd' and start_user[1] < 9:
                new_j += 1
            else:
                print('Invalid move')
                continue

            board.mss[start_user[0]][start_user[1]] = '[_]'

            start_user[0] = new_i
            start_user[1] = new_j

            board.mss[start_user[0]][start_user[1]] = c.player

            item_counter.counter(board.mss, start_user)

            board.show_pole()


def fill(board, itemlist, fillprosent):
    total_items = int(10 * fillprosent / 100)
    for _ in range(total_items):
        while True:
            rand_i = random.randint(0, 9)
            rand_j = random.randint(0, 9)
            if board.mss[rand_i][rand_j] == '[_]':
                board.mss[rand_i][rand_j] = random.choice(itemlist)
                break
class GameTimer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
    def start(self):
        self.start_time = time.time()
    def stop(self):
        self.end_time = time.time()
    def get_time(self):
        if self.start_time is None:
            return 0
        if self.end_time is None:
            return time.time() - self.start_time
        return self.end_time - self.start_time

class UseGame:
    def save_game(self, mss, player_pos, inventory, play_time):
        with open('save.txt', 'w') as f:
            f.write('10 10\n')
            for row in mss:
                f.write(' '.join(row) + '\n')
            f.write(f'{player_pos[0]} {player_pos[1]}\n')
            f.write(f"{inventory['C']} {inventory['A']} {inventory['D']} {inventory['H']}\n")
            f.write(str(play_time) + '\n')
        print('Game saved')
    def load_game(self):
        try:
            with open('save.txt', 'r') as f:
                lines = f.readlines()
            field = []
            for i in range(1, 11):
                field.append(lines[i].strip().split())
            player_pos = list(map(int, lines[11].split()))
            inv = list(map(int, lines[12].split()))
            inventory = {'C': inv[0], 'A': inv[1], 'D': inv[2], 'H': inv[3]}
            play_time = int(lines[13])
            print('Game loaded')
            return field, player_pos, inventory, play_time
        except FileNotFoundError:
            print('Save not found')
            return None
def hello():
    print('======================')
    print('   Start game')
    print('======================')
    print('1 - New Game')
    print('2 - Load Game')
    print('3 - Exit')

def open_table():
    with open('table.txt', 'r') as f:
        content = f.read()
        print(content)
user_table = input('Enter «1» to open the records table, any other symbol to skip:  ')
if user_table == '1':
    open_table()


player = Player(skin='*')

hello()
choice = input('Choose: ')
g = UseGame()
if choice == '1':
    print('New game started')
elif choice == '2':
    data = g.load_game()
    if data:
        mss, player_pos, inventory, play_time = data
else:
    print('Bye')

while True:
    intro_cat()

    pole = Pole()
    item_counter = ItemSum()

    items = ['[C]', '[A]', '[D]', '[H]']
    fill(pole, items, 40)

    user = UserHod()
    user.user(pole, item_counter)
    while True:
        timer = GameTimer()
        timer.start()
        move = input('user:  ')
        if move == 'q':
            timer.stop()
            print('You played:', int(timer.get_time()), 'seconds')
            break
    timer = GameTimer()
    timer.start()
