FROM python:3.10-slim

WORKDIR /app

COPY .. /app

# Install dependensi Python
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install openpyxl python-multipart

EXPOSE 8080

CMD ["python", "main.py"]
