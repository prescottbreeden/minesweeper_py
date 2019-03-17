class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __repr__(self):
        return "x:%i, y:%i" % (self.x, self.y)