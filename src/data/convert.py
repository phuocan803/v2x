import pickle as pkl
import pandas as pd

with open("all_data.pkl", "rb") as f:
    data = pkl.load(f)

df = pd.DataFrame(data)
df.to_csv("all_data.csv", index=False)