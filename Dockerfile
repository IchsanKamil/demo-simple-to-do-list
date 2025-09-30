# Simple web app Dockerfile
#FROM python:3.11-slim
#WORKDIR /app
#COPY . /app
#RUN pip install --no-cache-dir -r requirements.txt
#EXPOSE 5000
#CMD ["python", "app.py"]
# CMD ["flask", "run", "--host", "0.0.0.0","--port","5000"]

FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Cloud Run expects port from $PORT (default 8080)
EXPOSE 8080

# Use Gunicorn as the entrypoint (production server)
CMD exec gunicorn --bind :$PORT app:app
