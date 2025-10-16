#!/usr/bin/env bash
# Instala las librerías necesarias para compilar lxml
apt-get update && apt-get install -y libxml2-dev libxslt-dev python3-dev
pip install --upgrade pip
pip install -r requirements.txt