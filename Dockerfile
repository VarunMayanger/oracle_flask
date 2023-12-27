FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN apt-get update && \
    apt-get install -y libaio1 && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 9000
CMD ["python", "./python_db.py"]
