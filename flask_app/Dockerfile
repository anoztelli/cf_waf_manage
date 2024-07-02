# Base image olarak python:3.9-slim kullanılıyor
FROM python:3.9-slim

RUN pip install --no-cache-dir --upgrade pip
RUN pip install flask-cors

# Çalışma dizini olarak /app belirleniyor
WORKDIR /app

# Gereksinim dosyaları ekleniyor
COPY requirements.txt requirements.txt

# Gereksinim dosyaları yükleniyor
RUN pip install -r requirements.txt

# Tüm dosyalar ekleniyor
COPY . .


# Flask uygulaması başlatılıyor
CMD ["python", "app.py"]
