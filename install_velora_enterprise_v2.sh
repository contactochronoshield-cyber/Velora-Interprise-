#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "[1/12] Creando estructura..."

mkdir -p \
api \
database \
logs \
backups \
node-agent \
static/css \
static/js \
static/img \
static/video \
templates

touch database/velora.db
touch logs/velora.log

echo "[2/12] Instalando dependencias..."

pip install flask flask_sqlalchemy psutil requests python-dotenv gunicorn

echo "[3/12] Creando módulos..."

touch api/auth.py
touch api/customers.py
touch api/devices.py
touch api/monitoring.py
touch api/alerts.py
touch api/vch777.py

echo "[4/12] Creando agente..."

touch node-agent/agent.py

echo "[5/12] Creando Dashboard..."

touch templates/base.html
touch templates/dashboard.html
touch templates/customers.html
touch templates/devices.html
touch templates/monitoring.html
touch templates/vch777.html
touch templates/alerts.html
touch templates/settings.html
touch templates/login.html
touch templates/register.html

echo "[6/12] CSS..."

touch static/css/style.css

echo "[7/12] JavaScript..."

touch static/js/main.js

echo "[8/12] Recursos..."

mkdir -p static/img/backgrounds
mkdir -p static/img/icons

echo "[9/12] Base de datos..."

python - << PY

import sqlite3

db=sqlite3.connect("database/velora.db")
c=db.cursor()

c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT,email TEXT,password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY,company TEXT,email TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS devices(id INTEGER PRIMARY KEY,hostname TEXT,ip TEXT,status TEXT,cpu REAL,ram REAL,last_seen TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS alerts(id INTEGER PRIMARY KEY,title TEXT,severity TEXT,date TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS security_events(id INTEGER PRIMARY KEY,event TEXT,level TEXT,date TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS audit_logs(id INTEGER PRIMARY KEY,action TEXT,date TEXT)")

db.commit()
db.close()

print("DATABASE READY")

PY

echo "[10/12] Boot..."

chmod +x velora_boot.sh 2>/dev/null || true

echo "[11/12] Git..."

git add .

git commit -m "Velora Enterprise v2" || true

echo "[12/12] FINALIZADO"

echo ""
echo "====================================="
echo "VELORA ENTERPRISE INSTALADO"
echo "====================================="
echo ""
echo "Ejecuta:"
echo ""
echo "python app.py"
echo ""
echo "Repositorio:"
echo "https://github.com/contactochronoshield-cyber/Velora-Interprise-"
echo ""

