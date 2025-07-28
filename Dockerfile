FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Instalar herramientas del sistema
RUN apt-get update && apt-get install -y \
    curl unzip wget git perl ruby ruby-dev make build-essential \
    nmap whatweb wafw00f \
    && rm -rf /var/lib/apt/lists/*

# Instalar nikto
RUN git clone https://github.com/sullo/nikto.git /opt/nikto
ENV PATH="/opt/nikto:$PATH"

# Instalar nuclei
RUN curl -s https://api.github.com/repos/projectdiscovery/nuclei/releases/latest \
    | grep "browser_download_url.*linux_amd64.zip" \
    | cut -d '"' -f 4 \
    | wget -i - && unzip nuclei* && mv nuclei /usr/local/bin/ && rm nuclei*

# Directorio de trabajo
WORKDIR /app
COPY . /app

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
