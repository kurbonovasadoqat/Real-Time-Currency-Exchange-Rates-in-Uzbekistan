# ✅ Rasmiy Python 3.11 bazasi
FROM python:3.11-slim

# ✅ Ishchi katalog
WORKDIR /app

# ✅ Tizim kutubxonalarini o‘rnatish (aiohttp uchun zarur bo‘lgan gcc va ssl)
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ✅ Python kutubxonalarini o‘rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Loyiha fayllarini nusxalash
COPY . .

# ✅ Botni ishga tushirish
CMD ["python", "main.py"]
