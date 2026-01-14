class Player:
    def __init__(self, user_n=0, user_m=0, skin="*"):
        self.user_n = row
        self.user_m = col
        self.skin = skin

    def place(self, field):
        field[self.row][self.col] = self.skin
