import numpy as np

class Field(object):
    """docstring for Field"""
    def __init__(self, width=100, height=100):
        super(Field, self).__init__()
        self.width = width
        self.height = height
        self.t = 0
        self.field = np.zeros((height, width)).astype(np.int8)
        self.agents = []
        self.agent_size = 0

    def step(self):
        step_candidate = [[[]]]
        for agent in self.agents:
            x, y = agent.step(self.field[agent.y-1:agent.y+2][agent.x-1:agent.x+2])
            # 周期境界条件を適用
            x, y = x % self.width, y % self.height
            step_candidate[y][x].append(agent)
        for x, y in zip(range(self.width), range(self.height)):
            candidates = step_candidate[y][x]
            length = len(candidates)
            if length > 0:
                selected = candidates[np.randint(length)]
                selected.x = x
                selected.y = y
                self.field[y][x] = selected.id
        self.t += 1
        return t

    def add_agents(self, agents, sizes):
        for agent, size in zip(agents, sizes):
            for x, y in zip(np.random.randint(self.width, size), np.random.randint(self.height, size)):
                self.agents.append(agent.copy(x, y))
        incremental = np.sum(sizes)
        self.agent_size += incremental
        return incremental

    def get_agent_size(self):
        return self.agent_size
