FROM python:3.8

# usar outro workdir para desenvolvimento, corrigir proximas atualizações
WORKDIR /src

COPY requirements.txt ./
RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5000

CMD ["python", "src/app.py"]