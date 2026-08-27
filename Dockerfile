FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /app/backend
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
