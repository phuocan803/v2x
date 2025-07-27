"""
Chạy mô phỏng cho 1 xe (1 agent), lưu dữ liệu state, action, reward ra file.
"""

# python aggregate.py --input_dir ./data --output_file .data/all_data.pkl

from Environment import Environment
from agent import Agent
import os
import pickle

def main():
    # Đọc biến môi trường để xác định id xe
    vehicle_id = int(os.environ.get("VEHICLE_ID", 0))
    output_dir = os.environ.get("OUTPUT_DIR", "./data")
    os.makedirs(output_dir, exist_ok=True)

    # Khởi tạo môi trường và agent cho 1 xe
    env = Environment()
    agent = Agent()

    data = []
    state = env.reset()
    done = False
    while not done:
        action = agent.select_action(state)
        next_state, reward, done, info = env.step(action)
        data.append({
            "vehicle_id": vehicle_id,
            "state": state,
            "action": action,
            "reward": reward,
            "next_state": next_state
        })
        state = next_state

    # Lưu dữ liệu ra file
    with open(os.path.join(output_dir, f"vehicle_{vehicle_id}_data.pkl"), "wb") as f:
        pickle.dump(data, f)

if __name__ == "__main__":
    main()
