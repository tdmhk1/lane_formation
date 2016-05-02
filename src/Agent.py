class Agent(object):
    """docstring for Agent"""
    def __init__(self, name, x, y, dx, dy):
        super(Agent, self).__init__()
        self.name = name
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
