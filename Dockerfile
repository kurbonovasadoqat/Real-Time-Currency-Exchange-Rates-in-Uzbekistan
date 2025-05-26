# Dockerfile

FROM python:3.11-slim

WORKDIR /app

# ENV o'zgaruvchilar uchun
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Kerakli tizim paketlari
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ✅ Railway env-larni o‘qiy olishi uchun ENTRYPOINT yoki CMD faqat shu bo‘lishi kerak
CMD ["python", "main.py"]
