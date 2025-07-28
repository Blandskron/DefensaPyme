#!/bin/bash

# Nombre del entorno virtual
VENV_DIR=".venv"

echo "🚀 Creando entorno virtual en $VENV_DIR..."
python3 -m venv $VENV_DIR

echo "✅ Activando entorno virtual..."
source $VENV_DIR/Scripts/activate

echo "📦 Instalando dependencias Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔧 Instalando herramientas de escaneo (requiere sudo)..."
sudo apt-get update && sudo apt-get install -y \
  nmap \
  nikto \
  whatweb \
  wafw00f \
  curl \
  unzip \
  git

echo "🧠 Instalando nuclei..."
curl -s https://api.github.com/repos/projectdiscovery/nuclei/releases/latest \
| grep "browser_download_url.*linux_amd64.zip" \
| cut -d '"' -f 4 \
| wget -i - && unzip nuclei* && sudo mv nuclei /usr/local/bin/ && rm nuclei*

echo "✅ Instalación completa."

echo "🎯 Para iniciar el backend:"
echo "source $VENV_DIR/bin/activate && uvicorn app.main:app --reload"
