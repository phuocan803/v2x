# Sử dụng Python base image
FROM python:3.9-slim

WORKDIR /app

COPY ./src /app

RUN pip install --no-cache-dir -r requirements.txt

# Mặc định chạy single_vehicle.py
ENTRYPOINT ["python", "single_vehicle.py"]
