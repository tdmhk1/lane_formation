import numpy as np

class Agent(object):
    """docstring for Agent"""
    def __init__(self, id, x, y, dx, dy):
        super(Agent, self).__init__()
        if id == 0:
            raise("0 is invalid ID")
        self.id = id
        self.x = x
        self.y = y
        if dx**2 + dy**2 == 1:
            self.dx = dx
            self.dy = dy
        else:
            raise("velosity is not 1")

    def copy(self, x, y):
        return Agent(self.id, x, y, self.dx, self.dy)

    def equal(self, agent):
        return self.id == agent.id

    # 近傍の状態から次の移動先のx, y座標を返す
    def step(self, neighborhood):
        prob_dist = self.step_prob_dist(neighborhood)
        result = np.random.choice(9, p=prob_dist.reshape(9))
        return self.x + result % 3 - 1, self.y + result // 3 - 1

    def step_prob_dist(self, neighborhood, p_R11=0.25, p_L11=0.25, p_W11=0.5,
    p_R12=0.5, p_W12=0.5, p_L13=0.5, p_W13=0.5, p_R21=0.4, p_L21=0.1, p_W21=0.5,
    p_R22=0.5, p_W22=0.5, p_L23=0.1, p_W23=0.9, p_W3=0.5, p_B=0.5):
        x_F, y_F = 1+self.dx, 1+self.dy
        forward = neighborhood[y_F][x_F]
        # 正面にエージェントがいない場合
        if forward == 0:
            prob_dist = np.zeros((3, 3))
            prob_dist[y_F][x_F] = 1.0
        # 同じエージェントがいた場合
        elif forward == self.id:
            prob_dist = self._step_prob_dist_faced(neighborhood, p_R11, p_L11,
            p_W11, p_R12, p_W12, p_L13, p_W13, p_W3, p_B, True)
        # 異なるエージェントがいた場合
        else:
            prob_dist = self._step_prob_dist_faced(neighborhood, p_R21, p_L21,
            p_W21, p_R22, p_W22, p_L23, p_W23, p_W3, p_B, False)
        return prob_dist

    def _step_prob_dist_faced(self, neighborhood, p_R1, p_L1, p_W1, p_R2, p_W2,
    p_L3, p_W3, p_W4, p_B, is_same):
        x_R, y_R = 1+self.dx, 1-self.dy
        x_B, y_B = 1-self.dy, 1-self.dx
        x_L, y_L = 1-self.dx, 1+self.dy
        right = neighborhood[y_R][x_R]
        back = neighborhood[y_B][x_B]
        left = neighborhood[y_L][x_L]
        prob_dist = np.zeros((3, 3))
        # 両隣が空いている場合
        if right**2 + left**2 == 0:
            prob_dist[y_R][x_R] = p_R1
            prob_dist[y_L][x_L] = p_L1
            prob_dist[1][1] = p_W1
        # 両隣が埋まっている場合
        elif right * left != 0:
            if back == 0:
                prob_dist[1][1] = p_W4
                prob_dist[y_B][x_B] = p_B
            else:
                prob_dist[1][1] = 1.0
        # 両隣の一方のみ埋まっている場合
        else:
            if right == 0:
                prob_dist[y_R][x_R] = p_R2
                prob_dist[1][1] = p_W2
            else:
                prob_dist[y_L][x_L] = p_L3
                prob_dist[1][1] = p_W3
        return prob_dist
