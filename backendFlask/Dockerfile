FROM python:3

# usar outro workdir para desenvolvimento, corrigir proximas atualizações
WORKDIR /src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# CMD ["python", "app.py"]