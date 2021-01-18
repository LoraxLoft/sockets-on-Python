vertical_dict = [str(i+1) for i in range(8)]
gorizontal_dict = [chr(97+i) for i in range(8)]


class Checker:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def can_move(self, x, y):
        if abs(x-self.x) == 1 and y-self.y == 1 - 2*('w ' == self.color):
            return 1
        elif abs(x-self.x) == 2 and abs(y-self.y) == 2:
            return 2
        else:
            return 0


class Field:

    def __init__(self):
        self.field = [[None for i in range(8)] for j in range(8)]

    def fill_with_checkers(self):
        for i in range(1, 8, 2):
            self.field[0][i] = Checker(0, i, 'b ')
            self.field[2][i] = Checker(2, i, 'b ')
        for j in range(0, 8, 2):
            self.field[1][j] = Checker(1, j, 'b ')
        for i in range(0, 8, 2):
            self.field[5][i] = Checker(5, i, 'w ')
            self.field[7][i] = Checker(7, i, 'w ')
        for j in range(1, 8, 2):
            self.field[6][j] = Checker(6, j, 'w ')

    def go(self, x, y, color):
        pass

    def view(self):
        for i in range(8):
            for j in range(8):
                if self.field[i][j]:
                    print(self.field[i][j].color, end='')
                else:
                    print('_ ', end='')
            print('\n')


field = Field()
field.fill_with_checkers()
field.view()
