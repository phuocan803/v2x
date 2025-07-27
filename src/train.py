# """
# Huấn luyện DRL+GNN từ dữ liệu đã gom.
# """

# import pickle
# from agent import Agent

# def train_from_data(data_file):
#     with open(data_file, "rb") as f:
#         data = pickle.load(f)
#     agent = Agent()
#     agent.train_offline(data)
#     agent.save_model("trained_model.pth")
#     print("Đã train xong và lưu model.")

# if __name__ == "__main__":
#     import argparse
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--data_file", type=str, required=True)
#     args = parser.parse_args()
#     train_from_data(args.data_file)
