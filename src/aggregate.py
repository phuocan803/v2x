"""
Gom dữ liệu state-action-reward từ nhiều xe thành 1 file duy nhất.
"""

import os
import pickle

def aggregate_data(input_dir, output_file):
    all_data = []
    for fname in os.listdir(input_dir):
        if fname.endswith("_data.pkl"):
            with open(os.path.join(input_dir, fname), "rb") as f:
                all_data.extend(pickle.load(f))
    with open(output_file, "wb") as f:
        pickle.dump(all_data, f)
    print(f"Đã gom dữ liệu từ {input_dir} vào {output_file}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, required=True)
    parser.add_argument("--output_file", type=str, required=True)
    args = parser.parse_args()
    aggregate_data(args.input_dir, args.output_file)
