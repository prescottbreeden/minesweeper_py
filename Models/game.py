import json
from Models.square import Square
from Models.position import Position
from random import randint

class Game:
    def __init__(self, bombs):
        self.total_bombs = bombs
        self.size = bombs-2
        self.board = [] 
        self.create_board()
        self.generate_bombs()


    def create_board(self):
        for y in range(self.size):
            row = []
            for x in range(self.size):
                row.append(Square(x,y))
            self.board.append(row)


    def generate_bombs(self):
        bombs = []
        while len(bombs) < self.total_bombs:
            sq = self.add_bomb()
            bombs.append(sq)


    def add_warnings(self, pos):
        # increment sides
        self.inc_warn_top(pos)
        self.inc_warn_bottom(pos)
        self.inc_warn_right(pos)
        self.inc_warn_left(pos)

        # increment diagonals
        self.inc_warn_top_left(pos)
        self.inc_warn_bottom_left(pos)
        self.inc_warn_top_right(pos)
        self.inc_warn_bottom_right(pos)


    def add_bomb(self):
        x = randint(0,self.size-1)
        y = randint(0,self.size-1)
        pos = Position(x,y)
        sq = self.find_square(pos)
        if not sq.bomb:
            sq.bomb = True
            self.add_warnings(pos)
            return sq
        else:
            return self.add_bomb() 


    def inc_warn_top_left(self, pos):
        if pos.x > 0 and pos.y > 0: 
            loc = Position(pos.x-1, pos.y-1)
            sq = self.find_square(loc)
            sq.warning += 1


    def inc_warn_bottom_left(self, pos):
        if pos.x > 0 and pos.y < self.size-1: 
            loc = Position(pos.x-1, pos.y+1)
            sq = self.find_square(loc)
            sq.warning += 1


    def inc_warn_top_right(self, pos):
        if pos.x < self.size-1 and pos.y > 0: 
            loc = Position(pos.x+1, pos.y-1)
            sq = self.find_square(loc)
            sq.warning += 1


    def inc_warn_bottom_right(self, pos):
        if pos.x < self.size-1 and pos.y < self.size-1: 
            loc = Position(pos.x+1, pos.y+1)
            sq = self.find_square(loc)
            sq.warning += 1


    def inc_warn_top(self, pos):
        if pos.y == 0: return
        loc = Position(pos.x, pos.y-1)
        sq = self.find_square(loc)
        sq.warning += 1
        

    def inc_warn_bottom(self, pos):
        if pos.y == self.size-1: return
        loc = Position(pos.x, pos.y+1)
        sq = self.find_square(loc)
        sq.warning += 1


    def inc_warn_right(self, pos):
        if pos.x == self.size-1: return
        loc = Position(pos.x+1, pos.y)
        sq = self.find_square(loc)
        sq.warning += 1
    
    
    def inc_warn_left(self, pos):
        if pos.x == 0: return
        loc = Position(pos.x-1, pos.y)
        sq = self.find_square(loc)
        sq.warning += 1


    def print_board(self):
        print(self.board)


    def find_square(self, pos):
        return self.board[pos.x][pos.y]


    def to_json(self):
        return json.dumps(self, 
                default=lambda g: g.__dict__, sort_keys=True, indent=4)



