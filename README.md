# Hệ thống mô phỏng và huấn luyện phân bổ tài nguyên V2X dùng GNN + DRL

## Kiến trúc

- Mỗi xe (V2V agent) chạy trong 1 container độc lập.
- Sử dụng Kubernetes để scale số lượng xe.
- Dữ liệu state-action-reward của từng xe được gom lại để huấn luyện tập trung.

## Thư mục

- `src/`: Code Python chính (mô phỏng, gom dữ liệu, train).
- `docker/`: Dockerfile.
- `k8s/`: File YAML cho Kubernetes.
- `scripts/`: Script hỗ trợ.

## Hướng dẫn

```
no Docker flow: main -> aggregate -> train
```


### 1. Build Docker image

```bash
cd docker
docker build -t quocanuit/v2v-agent:latest .

docker push quocanuit/v2v-agent:latest
```

### 2. Deploy lên Kubernetes

```bash
kubectl apply -f k8s/v2v-data-pvc.yaml
kubectl apply -f k8s/v2v-deployment.yaml
```

- Sửa `replicas` trong `v2v-deployment.yaml` để scale số lượng xe.

### 3. Thu thập dữ liệu

- Dữ liệu của từng xe sẽ được lưu trong PVC `/data` (mỗi file: `vehicle_{id}_data.pkl`).
- Sau khi chạy xong, copy dữ liệu về máy local:

```bash
kubectl cp <pod-name>:/data ./data
```

### 4. Gom dữ liệu

```bash
python src/aggregate.py --input_dir ./data --output_file ./all_data.pkl
```

### 5. Train tập trung

```bash
python src/train_multi.py --data_file ./all_data.pkl
```

## Ghi chú

- Có thể chỉnh sửa code trong `src/` để thay đổi logic mô phỏng hoặc huấn luyện.
- Đảm bảo các file không cần thiết đã được xóa khỏi repo.

## Liên hệ

- Liên hệ nhóm phát triển để được hỗ trợ thêm.
