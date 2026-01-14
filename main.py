# M = monster
# D = damage
# H = health
# C = coin

import random

minefield = []
user_field = []

def create_minefield(field, size_a, size_b):
    for a in range(11):
        field.append([])
        for b in range(11):
            field[a].append('[_]')

def create_user_field(field, size_n, size_m):
    for n in range(11):
        field.append([])
        for m in range(11):
            field[n].append('[_]')

def show_user_field(field, size_n, size_m):
    for m in range(11):
        print('   ', end='')
    print()
    for n in range(11):
        print(' ', ' ', end='')
        for m in range(size_m):
            print(field[n][m], ' ', end='')
        print()
      
def show_minefield(minefield, size_a, size_b):
  for a in range(11):
      print('   ', end='')
  print()
  for b in range(11):
      print(' ', ' ', end='')
      for a in range(size_a):
          print(minefield[a][b], ' ', end='')
      print()

size_a = size_n = 10

size_b = size_m = 10

def placing_items(minefield, size_a, size_b, items_number):
    for i in range(items_number):
        while True:
            rand_a = random.randint(0, size_a - 1)
            rand_b = random.randint(0, size_b - 1)
            if minefield[rand_a][rand_b] == '[_]':
              minefield[rand_a][rand_b] = random.choice(['[C]', '[U]', '[D]', '[H]'])

              break

def user(user_n, user_m, user_choice = input("Please enter the directio in which you want to move (W,A,S,D):")):
  
  for i in range(len(minefield)):
    if user_choice == 'W':
      user_field[user_n][user_m] = user_field[i-1][0] = 'X'
    if user_choice == 'S':
      user_field[user_n][user_m] = user_field[i+1][0] = 'X'
    if user_choice == 'D':
      user_field[user_n][user_m] = user_field[0][i+1] = 'X'
    if user_choice == 'S':
      user_field[user_n][user_m] = user_field[0][i-1] = 'X'

# def flag(user_field, size_n, size_m):
#     user_n = int(input('Enter row of the cell you want to flag: '))
#     user_m = int(input('Enter column the cell you want to flag: '))
#     user_field[user_n][user_m] = '[#]'
#     show_user_field(user_field, size_n, size_m)

create_minefield(minefield, size_a, size_b)
create_user_field(user_field, size_n, size_m)
placing_items(minefield, size_a, size_b, 10)
show_user_field(user_field, size_n, size_m)
show_minefield(minefield, size_a, size_b)
user(user_n, user_m, user_choice = input("Please enter the directio in which you want to move (W,A,S,D)"))
