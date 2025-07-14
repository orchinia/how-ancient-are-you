FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run Flask app
CMD ["python", "src/app.py", "--debug"]
