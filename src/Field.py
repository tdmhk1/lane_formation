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
        step_candidates = [[[] for _ in range(self.width)] for _ in range(self.height)]
        for agent in self.agents:
            neighborhood = self._get_neighberhood(agent.x, agent.y)
            x, y = agent.step(neighborhood)
            # 周期境界条件を適用
            x, y = x % self.width, y % self.height
            step_candidates[y][x].append(agent)
        for x in range(self.width):
            for y in range(self.height):
                candidates = step_candidates[y][x]
                length = len(candidates)
                if length > 0:
                    selected = candidates[np.random.randint(length)]
                    if x != selected.x or y != selected.y: 
                        self.field[y][x] = selected.id
                        self.field[selected.y][selected.x] = 0
                        selected.x, selected.y = x, y
        self.t += 1
        return self.t

    def add_agents(self, agents, sizes):
        for agent, size in zip(agents, sizes):
            for i in range(size):
                x, y = self._generate_point()
                self.agents.append(agent.copy(x, y))
                self.field[y][x] = agent.id
        incremental = np.sum(sizes)
        self.agent_size += incremental
        return incremental

    def add_agent(self, agent):
        if self.field[agent.y][agent.x] == 0:
            self.field[agent.y][agent.x] = agent.id
            self.agents.append(agent)
        else:
            raise("field is already filled")
        return agent
        
    def get_field(self):
        return self.field

    def get_agent_size(self):
        return self.agent_size

    def _get_neighberhood(self, x, y):
        neighborhood = np.zeros((3, 3)).astype(np.int8)
        for i in range(3):
            for j in range(3):
                neighborhood[i][j] = self.field[(y-1+i)%self.height][(x-1+j)%self.width]
        return neighborhood

    def _generate_point(self):
        x, y = -1, -1
        while x < 0 or self.field[y][x] != 0:
            x = np.random.randint(self.width)
            y = np.random.randint(self.height)
        return x, y
