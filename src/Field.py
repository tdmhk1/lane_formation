import numpy as np

class Field(object):
    """docstring for Field"""
    def __init__(self, width=100, height=100, t=0):
        super(Field, self).__init__()
        self.width = width
        self.height = height
        self.t = t
        self.field = np.zeros((height, width))
        self.agents = []

    def step(self, arg):
        t += 1
        return t

    def add_agent(self, agent):
        if field[agent.x][agent.y] != 0:
            raise InputError("already filled")
        else:
            field[agent.x][agent.y] = agent.name
            self.agents.append(agent)
        return agent
