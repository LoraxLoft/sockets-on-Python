import socket


class Field:

    def __init__(self):
        field = [[None for i in range(8)] for i in range(8)]

    def fill_with_checkers(self):
        pass


class Checker:

    def __init__(self, x, y, color, field):
        self.coord_x = x
        self.coord_y = y
        self.color = color
        self.field = field

    def move(self, x, y):
        if self.can_go_there(x, y):
            self.coord_x = x
            self.coord_y = y
            return True
        else:
            return False

    def can_go_thee(self, x, y):
        pass


class Game:

    def __init__(self):
        self.field = [[None for i in range(8)] for j in range(8)]
        self.turn = False
        self.start = False

    def find_game(self):
        sock.send(b'find game')
        print("Looking for a game...")
        data = sock.recv(1024)
        if data[0] == 'start':
            self.start = True
            self.turn = data[1]

    def play(self):
        pass

    def update_field(self, go):
        pass

    def view_field(self):
        for i in range(8):
            for j in range(8):
                if not self.field[i][j]:
                    print('_ ')
                elif self.field[i][j] == 1:
                    print('w ')
                else:
                    print('b ')
            print('\n')


sock = socket.socket()
sock.connect(('localhost', 9090))

game = Game()
game.find_game()

sock.close()
