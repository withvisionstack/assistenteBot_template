FROM python:3.14.3

WORKDIR /primeiro bot

COPY requiriments.txt .

RUN pip install --no-cache-dir -r requiriments.txt

COPY . .

CMD ["python", "main.py"]
