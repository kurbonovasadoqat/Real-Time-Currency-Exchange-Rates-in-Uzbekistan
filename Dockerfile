# ✅ Python bazasi
FROM python:3.11-slim

# ✅ Ishchi katalog
WORKDIR /app

# ✅ Tizim kutubxonalarini o‘rnatish (aiohttp, C compiler uchun zarur)
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# ✅ Requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# ✅ Ilovani ko‘chirish
COPY . .

# ✅ Botni ishga tushirish
CMD ["python", "main.py"]
