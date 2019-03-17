import json
from Models.square import Square
from Models.position import Position
from random import randint

class Game:
    def __init__(self, size):
        self.total_bombs = size
        self.board = [] 
        self.create_board()
        self.generate_bombs()


    def create_board(self):
        for x in range(self.total_bombs):
            row = []
            for y in range(self.total_bombs):
                row.append(Square(x,y))
            self.board.append(row)


    def generate_bombs(self):
        bombs = []
        while len(bombs) < self.total_bombs:
            loc = self.add_bomb()
            bombs.append(loc)
        print(bombs)


    def add_warnings(self, pos):
        # increment sides
        if pos.y > 0: self.inc_warn_top(pos)
        if pos.y < 9: self.inc_warn_bottom(pos)
        if pos.x < 9: self.inc_warn_right(pos)
        if pos.x > 0: self.inc_warn_left(pos)

        # increment diagonals
        if pos.x > 0 and pos.y > 0: 
            self.inc_warn_top_left(pos)
        if pos.x < 9 and pos.y < 0: 
            self.inc_warn_top_right(pos)
        if pos.x < 9 and pos.y < 9: 
            self.inc_warn_bottom_right(pos)
        if pos.x > 0 and pos.y < 9: 
            self.inc_warn_bottom_left(pos)


    def add_bomb(self):
        x = randint(0,9)
        y = randint(0,9)
        pos = Position(x,y)
        sq = self.find_square(pos)
        if not sq.bomb:
            sq.bomb = True
            self.add_warnings(pos)
            return sq
        else:
            self.add_bomb() 


    # relational coordinate map:
    # top:          y-1 x
    # top right:    y-1 x+1 
    # right:        y   x+1
    # bottom right: y+1 x+1
    # bottom:       y+1 x
    # bottom left:  y-1 x-1
    # left:         y   x-1
    # top left:     y-1 x-1

    def inc_warn_top_left(self, pos):
        pos.y -= 1
        pos.x -= 1
        sq = self.find_square(pos)
        sq.warning += 1


    def inc_warn_bottom_left(self, pos):
        pos.y -= 1
        pos.x += 1
        sq = self.find_square(pos)
        sq.warning += 1


    def inc_warn_top_right(self, pos):
        pos.y -= 1
        pos.x += 1
        sq = self.find_square(pos)
        sq.warning += 1


    def inc_warn_bottom_right(self, pos):
        pos.y += 1
        pos.x += 1
        sq = self.find_square(pos)
        sq.warning += 1


    def inc_warn_top(self, pos):
        pos.y -= 1
        sq = self.find_square(pos)
        sq.warning += 1


    def inc_warn_bottom(self, pos):
        pos.y += 1
        sq = self.find_square(pos)
        sq.warning += 1


    def inc_warn_right(self, pos):
        pos.x += 1
        sq = self.find_square(pos)
        sq.warning += 1
    
    
    def inc_warn_left(self, pos):
        pos.x -= 1
        sq = self.find_square(pos)
        sq.warning += 1


    def print_board(self):
        print(self.board)


    def find_square(self, pos):
        return self.board[pos.x][pos.y]


    def to_json(self):
        return json.dumps(self, 
                default=lambda g: g.__dict__, sort_keys=True, indent=4)


