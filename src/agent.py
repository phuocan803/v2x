import numpy as np
import random

class Agent:
    def __init__(self, state_size=4, action_size=2):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = 0.95  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        # Đơn giản hóa: dùng numpy thay vì deep learning framework
        # Thực tế nên dùng keras/torch, ở đây chỉ mockup
        return None

    def _policy(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        # Giả lập Q-value, thực tế: self.model.predict(state)
        return 0

    def select_action(self, state):
        return self._policy(state)

    def train_offline(self, data):
        # Đơn giản hóa: chỉ lưu vào memory
        for sample in data:
            self.memory.append((sample["state"], sample["action"], sample["reward"], sample["next_state"]))
        # Thực tế: cập nhật model ở đây

    def save_model(self, path):
        # Giả lập lưu model
        with open(path, 'w') as f:
            f.write('model weights')