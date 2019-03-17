class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.warning = 0
        self.revealed = False
        self.bomb = False


    def __repr__(self):
        return "\n x:%s, y:%s, bomb:%r, warning:%i" % (
            self.x, self.y, self.bomb, self.warning)