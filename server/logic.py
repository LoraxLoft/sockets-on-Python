vertical_dict = [chr(i + 49) for i in range(8)]
gorizontal_dict = [chr(97 + i) for i in range(8)]
colors = ['w', 'b']


def parse(code):
    return gorizontal_dict.index(code[0]), vertical_dict.index(code[1])


class Checker:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self, x, y):
        self.x = x
        self.y = y

    def can_move(self, x, y):
        if abs(x - self.x) == 1 and y - self.y == 1 - 2 * ('b' == self.color):
            return 1
        elif abs(x - self.x) == 2 and abs(y - self.y) == 2:
            return 2
        else:
            return 0


class Field:

    def __init__(self):
        self.field = [[None for i in range(8)] for j in range(8)]
        self.turn_color = 'w'

    def fill_with_checkers(self):
        for i in range(1, 8, 2):
            self.field[i][0] = Checker(i, 0, 'w')
            self.field[i][2] = Checker(i, 2, 'w')
        for j in range(0, 8, 2):
            self.field[j][1] = Checker(j, 1, 'w')
        for i in range(0, 8, 2):
            self.field[i][5] = Checker(i, 5, 'b')
            self.field[i][7] = Checker(i, 7, 'b')
        for j in range(1, 8, 2):
            self.field[j][6] = Checker(j, 6, 'b')

    def go(self, from_code, to_code):
        x_from, y_from = parse(from_code)
        x_to, y_to = parse(to_code)
        checker_moved = self.field[x_from][y_from]
        if not checker_moved:
            return "There is no checker on this field"
        elif checker_moved.color != self.turn_color:
            return "Its not your turn to go"
        else:
            action = checker_moved.can_move(x_to, y_to)
            if not action:
                return "Check cannot go there"
            elif self.field[x_to][y_to]:
                return "Checker can go only to an empty field"
            elif action == 1:
                checker_moved.move(x_to, y_to)
                self.field[x_to][y_to] = checker_moved
                self.field[x_from][y_from] = None
            else:
                checker_fought = self.field[x_from + (x_to - x_from) // 2][y_from + (y_to - y_from) // 2]
                if not checker_fought:
                    return "Check can go there only to fight. No one to fight"
                elif checker_fought.color == checker_moved.color:
                    return "You cannot fight your figure"
                else:
                    checker_moved.move(x_to, y_to)
                    self.field[x_to][y_to] = checker_moved
                    self.field[x_from][y_from] = None
                    self.field[x_from + (x_to - x_from) // 2][y_from + (y_to - y_from) // 2] = None

    def any_to_beat(self):



    def view(self):
        print(' ', end=' ')
        for i in range(8):
            print(gorizontal_dict[i], end=' ')
        print()
        for i in range(8):
            print(vertical_dict[i], end=' ')
            for j in range(8):
                check = self.field[j][i]
                if check:
                    print(check.color, end=' ')
                else:
                    print('_', end=' ')
            print()



field = Field()
field.fill_with_checkers()
field.view()

while input("go?") != "exit":
    go_who = input("Who goes")
    go_where = input("Where goes")
    res = field.go(go_who, go_where)
    if res:
        print(res)
    else:
        field.turn_color = colors[(colors.index(field.turn_color)+1) % 2]
        print(colors.index(field.turn_color), (colors.index(field.turn_color)+1) % 2)
    field.view()


