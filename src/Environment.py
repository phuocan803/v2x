import numpy as np

class Environment:
    def __init__(self):
        self.state = None
        self.steps = 0
        self.max_steps = 100

    def reset(self):
        self.state = np.zeros(4)  # ví dụ: trạng thái 4 chiều
        self.steps = 0
        return self.state

    def step(self, action):
        # Đơn giản hóa: random next state, reward
        self.state = np.random.rand(4)
        reward = np.random.rand()  # hoặc logic reward thực tế
        self.steps += 1
        done = self.steps >= self.max_steps
        info = {}
        return self.state, reward, done, info