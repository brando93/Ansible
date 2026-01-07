FROM python:3.11-slim

# Evita archivos .pyc y logs raros
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY app ./app

# Puerto interno FIJO (no confundir con el host)
EXPOSE 8000

# Comando estándar
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]