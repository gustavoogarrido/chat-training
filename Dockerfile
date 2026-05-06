FROM python:3.11-slim

WORKDIR /project

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar projeto
COPY . .

# Dar permissão ao script de inicialização
RUN chmod +x start.sh

# Rodar script que inicializa backend e frontend
CMD ["./start.sh"]
