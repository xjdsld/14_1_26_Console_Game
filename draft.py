import random

mss = [] 
for i in range (10): 
    mss.append([]) 
    for j in range(10):
            mss[i].append('[_]')

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
      print('Number of C',sum(self.mss_c))
      print('Number of A',sum(self.mss_a))
      print('Number of D',sum(self.mss_d))
      print('Number of H',sum(self.mss_h))

    def counter(self, mss):
        start_user = [0, 0]
        i = ItemSum()

        cell = mss[start_user[0]][start_user[1]]

        if cell == '[C]':
            self.mss_c.append(1)
            i.print_user_case()
            mss[start_user[0]][start_user[1]] = '[_]'
        elif cell == '[A]':
            self.mss_a.append(1)
            i.print_user_case()
            mss[start_user[0]][start_user[1]] = '[_]'
        elif cell == '[D]':
            self.mss_d.append(1)
            i.print_user_case()
            mss[start_user[0]][start_user[1]] = '[_]'
        elif cell == '[H]':
            i.print_user_case()
            self.mss_h.append(1)
            mss[start_user[0]][start_user[1]] = '[_]'

class Player:
    def __init__(self, user_n=0, user_m=0, skin="*"):
        self.user_n = row
        self.user_m = col
        self.skin = skin

    def place(self, field):
        field[self.row][self.col] = self.skin

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
    print('Crit bonus: +' + str(int(bonus*100)) + '%')
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

    def user(self, mss):
    
        start_user = [0, 0]
        c = Cell()
    
        mss[start_user[0]][start_user[1]] = c.player
    
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
    
            mss[start_user[0]][start_user[1]] = '[_]'
    
            start_user[0] = new_i
            start_user[1] = new_j
    
            mss[start_user[0]][start_user[1]] = c.player

def fill(mss, itemlist, fillprosent):
    for i in range(10 * fillprosent / 100):
        items = itemlist.length()
        while True:
            rand_i = randint(0, 9)
            rand_j = randint(0, 9)
            if mss[rand_i][rand_j] == '[_]':
                mss[rand_i][rand_j] = ('[', itemlist[items], ']')
                break
