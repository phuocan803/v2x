

## 1. Kiến trúc 

- Mỗi xe (agent) chạy trong một container độc lập.
- Có thể scale số lượng xe dễ dàng với Kubernetes.
- Dữ liệu state, action, reward của từng xe được lưu riêng, sau đó gom lại để huấn luyện tập trung.

## 2. Cấu trúc thư mục

```
src/
  ├── main.py           # Mô phỏng cho 1 agent (xe)
  ├── agent.py          # Định nghĩa agent và logic chọn hành động
  ├── Environment.py    # Mô phỏng môi trường
  ├── aggregate.py      # Gom dữ liệu từ nhiều xe
  ├── train.py          # Huấn luyện offline từ dữ liệu gom
  ├── data/
  │     ├── all_data.pkl
  │     ├── all_data.csv
  │     └── convert.py  # Chuyển đổi dữ liệu sang CSV
k8s/
  ├── v2v-deployment.yaml   # Triển khai nhiều agent trên Kubernetes
  └── v2v-data-pvc.yaml     # PersistentVolumeClaim cho lưu trữ dữ liệu
requirements.txt
```

---

## 3. Hướng dẫn 

### Cài đặt 

```bash
pip install -r src/requirements.txt
```

### Chạy mô phỏng cho 1 agent (xe)

```bash
python src/main.py
```
- Có thể đặt biến môi trường `VEHICLE_ID` và `OUTPUT_DIR` để tùy chỉnh.

### Gom dữ liệu từ nhiều agent

```bash
python src/aggregate.py --input_dir src/data --output_file src/data/all_data.pkl
```

### Chuyển đổi dữ liệu sang CSV

```bash
python src/data/convert.py
```

### Huấn luyện offline từ dữ liệu gom

```bash
python src/train.py --data_file src/data/all_data.pkl
```

---

## 4. Triển khai phân tán với Kubernetes

### Build Docker image (nếu cần)

```bash
docker build -t quocanuit/v2v-agent:latest .
docker push quocanuit/v2v-agent:latest
```

### Deploy lên Kubernetes

```bash
kubectl apply -f k8s/v2v-data-pvc.yaml
kubectl apply -f k8s/v2v-deployment.yaml
```
- Sửa trường `replicas` trong `v2v-deployment.yaml` để thay đổi số lượng xe.

### Thu thập dữ liệu từ PVC

```bash
kubectl cp <pod-name>:/data ./data
```
- Dữ liệu của từng xe sẽ được lưu trong PVC `/data` (mỗi file: `vehicle_{id}_data.pkl`).

---

